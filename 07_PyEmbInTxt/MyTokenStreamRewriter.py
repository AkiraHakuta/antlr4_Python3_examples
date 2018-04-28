from antlr4.TokenStreamRewriter import TokenStreamRewriter

class MyTokenStreamRewriter(TokenStreamRewriter):
    
    # from antlr4\TokenStreamRewriter.py class TokenStreamRewriter(object):
    # def _reduceToSingleOperationPerIndex(self, rewrites) override
    def _reduceToSingleOperationPerIndex(self, rewrites):
        # Walk replaces
        for i, rop in enumerate(rewrites):
            if any((rop is None, not isinstance(rop, MyTokenStreamRewriter.ReplaceOp))):
                continue
            # Wipe prior inserts within range
            inserts = [op for op in rewrites[:i] if isinstance(rop, MyTokenStreamRewriter.InsertBeforeOp)]
            for iop in inserts:
                if iop.index == rop.index:
                    rewrites[iop.instructionIndex] = None
                    if rop.text != None:
                        rop.text = '{}{}'.format(iop.text, rop.text)
                    else:
                        rop.text = '{}'.format(iop.text)
                elif all((iop.index > rop.index, iop.index <= rop.last_index)):
                    rewrites[iop.instructionIndex] = None

            # Drop any prior replaces contained within
            prevReplaces = [op for op in rewrites[:i] if isinstance(op, MyTokenStreamRewriter.ReplaceOp)]
            for prevRop in prevReplaces:
                if all((prevRop.index >= rop.index, prevRop.last_index <= rop.last_index)):
                    rewrites[prevRop.instructioIndex] = None
                    continue
                isDisjoint = any((prevRop.last_index<rop.index, prevRop.index>rop.last_index)) # rop  -> rop.last_index
                #isSame = all((prevRop.index == rop.index, prevRop.last_index == rop.last_index)) # deleted
                if all((prevRop.text is None, rop.text is None, not isDisjoint)):
                    rewrites[prevRop.instructioIndex] = None
                    rop.index = min(prevRop.index, rop.index)
                    rop.last_index = min(prevRop.last_index, rop.last_index)
                    print('New rop {}'.format(rop))
                elif not isDisjoint:  # not all((isDisjoint, isSame)) -> not isDisjoint
                    raise ValueError("replace op boundaries of {} overlap with previous {}".format(rop, prevRop))

        # Walk inserts
        for i, iop in enumerate(rewrites):
            if any((iop is None, not isinstance(iop, MyTokenStreamRewriter.InsertBeforeOp))):
                continue
            prevInserts = [op for op in rewrites[:i] if isinstance(iop, MyTokenStreamRewriter.InsertBeforeOp)]
            for prevIop in prevInserts:
                if prevIop.index == iop.index:
                    iop.text += prevIop.text
                    rewrites[i] = None
            # look for replaces where iop.index is in range; error
            prevReplaces = [op for op in rewrites[:i] if isinstance(op, MyTokenStreamRewriter.ReplaceOp)]
            for rop in prevReplaces:
                if iop.index == rop.index:
                    rop.text = iop.text + rop.text
                    rewrites[i] = None
                    continue
                if all((iop.index >= rop.index, iop.index <= rop.index)):
                    raise ValueError("insert op {} within boundaries of previous {}".format(iop, rop))

        reduced = {} # outdented
        for i, op in enumerate(rewrites):
            if op is None: continue
            if reduced.get(op.index) != None: raise ValueError('should be only one op per index')
            reduced[op.index] = op

        return reduced