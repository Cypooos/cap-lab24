"""
CAP, SSA Intro, Elimination and Optimisations
Functions to convert a CFG out of SSA Form.
"""

from typing import cast, List
from Lib import RiscV
from Lib.CFG import Block, BlockInstr, CFG
from Lib.Operands import Temporary
from Lib.Statement import AbsoluteJump, Label
from Lib.Terminator import BranchingTerminator, Return
from Lib.PhiNode import PhiNode
from TP05.SequentializeMoves import sequentialize_moves
from random import randint # to generate the label name of the in-beetween block

def generate_moves_from_phis(phis: List[PhiNode], parent: Block, me:Block) -> List[BlockInstr]:
    """
    `generate_moves_from_phis(phis, parent)` builds a list of move instructions
    to be inserted in a new block between `parent` and the block with phi nodes
    `phis`.

    This is an helper function called during SSA exit.
    """
    moves: List[BlockInstr] = []
    for phi in phis:
        phi_final_var = phi.var
        dictio = phi.get_srcs()
        variable = dictio.get(parent.get_label(),None)
        if variable == None: continue
        to_add = RiscV.mv(phi_final_var, variable)
        moves.append(to_add)
    return moves


def exit_ssa(cfg: CFG, is_smart: bool) -> None:
    """
    `exit_ssa(cfg)` replaces phi nodes with move instructions to exit SSA form.

    `is_smart` is set to true when smart register allocation is enabled (Lab 5b).
    """
    for b in cfg.get_blocks():
        phis = cast(List[PhiNode], b.get_phis())  # Use cast for Pyright
        b.remove_all_phis()  # Remove all phi nodes in the block
        parents: List[Block] = b.get_in().copy()
        
        for parent in parents:
            
            # print("DOING",parent.get_label()," --> ",b.get_label())

            moves = generate_moves_from_phis(phis, parent, b)

            # make the new block
            b_label = b.get_label()
            new_terminator = AbsoluteJump(b_label)
            new_label = Label("phi_"+parent.get_label().name+"__to__"+b.get_label().name+"_r"+str(randint(10000,99999)))
            new_block = Block(new_label,moves,new_terminator)
            cfg.add_block(new_block)

            # change the parent's terminator
            termi = parent.get_terminator()
            if isinstance(termi, AbsoluteJump):
                if termi.label == b_label: termi.label = new_label 
            elif isinstance(termi, BranchingTerminator):
                if termi.label_else == b_label: termi.label_else = new_label 
                if termi.label_then == b_label: termi.label_then = new_label 
            elif isinstance(termi, Return):
                pass
            
            # change the edges
            cfg.remove_edge(parent,b)
            cfg.add_edge(parent,new_block)
            cfg.add_edge(new_block,b)