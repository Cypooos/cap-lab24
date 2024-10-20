"""
CAP, CodeGeneration, CFG construction from linear code
"""

from typing import List
from Lib.Errors import MiniCInternalError
from Lib.FunctionData import FunctionData
from Lib.LinearCode import LinearCode, CodeStatement
from Lib.Statement import (
    Instru3A, Comment, Label, AbsoluteJump, ConditionalJump
)
from Lib.Terminator import jump2terminator
from Lib.CFG import Block, BlockInstr, CFG


def find_leaders(instructions: List[CodeStatement]) -> List[int]:
    """
    Find the leaders in the given list of instructions as linear code.
    Returns a list of indices in the instruction list whose first is 0 and
    last is len(instructions)
    """
    leaders: List[int] = [0]
    for i,instruction in enumerate(instructions):
        if isinstance(instruction,Label): leaders.append(i)
        if isinstance(instruction,ConditionalJump): leaders.append(i+1)
    leaders.append(len(instructions))
    return leaders


def separate_with_leaders(instructions: List[CodeStatement],
                          leaders: List[int]) -> List[List[CodeStatement]]:
    """
    Partition the lists instructions into a list containing for
    elements the lists of statements between indices
    leaders[i] (included) and leaders[i+1] (excluded).

    If leaders[i] = leaders[i+1], do not add the empty list.
    """
    chunks: List[List[CodeStatement]] = []
    for i in range(0, len(leaders)-1):
        start = leaders[i]
        end = leaders[i+1]
        if start != end:
            # Avoid corner-cases when a label immediately follows a jump
            chunks.append(instructions[start:end])
    return chunks


def prepare_chunk(pre_chunk: List[CodeStatement], fdata: FunctionData) -> tuple[
                  Label, ConditionalJump | AbsoluteJump | None, List[BlockInstr]]:
    """
    Extract the potential label (respectively jump)
    at the start (respectively end) of the list instrs_chunk,
    and return the tuple with this label, this jump and the
    rest of instrs_chunk.

    If there is no label at the start then return a fresh label instead,
    thanks to fdata (use `fdata.fresh_label(fdata._name)` for instance).
    If there is no jump at the end, return None instead.

    Raise an error if there is a label not in first position in pre_chunk,
    or a jump not in last position.
    """
    label:Label
    jump:ConditionalJump | AbsoluteJump | None = None
    inner_statements: List[CodeStatement] = pre_chunk
    # Extract the first instruction from inner_statements if it is a label, or create a fresh one
    if isinstance(pre_chunk[0],Label):
        label_ins = pre_chunk.pop(0)
        assert isinstance(label_ins,Label)
        label = label_ins
    else:
        label = fdata.fresh_label("leader_label")

    # Extract the last instruction from inner_statements if it is a jump, or do nothing
    
    if pre_chunk != [] and isinstance(pre_chunk[-1],(ConditionalJump,AbsoluteJump)):
        jump_ins = pre_chunk.pop(-1)
        assert isinstance(jump_ins,(ConditionalJump,AbsoluteJump))
        jump = jump_ins

    # Check that there is no other label or jump left in inner_statements
    l: List[BlockInstr] = []
    for i in inner_statements:
        match i:
            case AbsoluteJump() | ConditionalJump():
                raise MiniCInternalError(
                    "prepare_chunk: Jump {} not in last position of a chunk"
                    .format(i))
            case Label():
                raise MiniCInternalError(
                    "prepare_chunk: Label {} not in first position of a chunk"
                    .format(i))
            case Instru3A() | Comment():
                l.append(i)
    return (label, jump, l)


def build_cfg(linCode: LinearCode) -> CFG:
    """Extract the blocks from the linear code and add them to the CFG."""
    fdata = linCode.fdata
    cfg = CFG(fdata)
    instructions = linCode.get_instructions()
    # 1. Identify Leaders
    leaders = find_leaders(instructions)
    # 2. Extract Chunks of Instructions
    pre_chunks: List[List[CodeStatement]] = separate_with_leaders(instructions, leaders)
    chunks: List[tuple[Label, ConditionalJump | AbsoluteJump | None, List[BlockInstr]]] = [
        prepare_chunk(pre_chunk, fdata) for pre_chunk in pre_chunks]
    # 3. Build the Blocks
    next_label = None
    for (label, jump, block_instrs) in reversed(chunks):
        term = jump2terminator(jump, next_label)
        block = Block(label, block_instrs, term)
        cfg.add_block(block)
        next_label = label
    # 4. Fill the edges
    for block in cfg.get_blocks():
        for dest in cfg.out_blocks(block):
            cfg.add_edge(block, dest)
    # 5. Identify the entry label of the CFG
    cfg.set_start(chunks[0][0])
    return cfg
