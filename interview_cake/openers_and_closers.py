
def braces_validators(braces):
    closure_hash = {'(':')','{':'}','[':']'}
    brace_stack = []
    for brace in braces:
        if brace in closure_hash:
            brace_stack.append(closure_hash[brace])
        else:
            if len(brace_stack):
                last_brace = brace_stack.pop()
                if last_brace == brace:
                    continue
            return False
    return True

braces_validators("{[(])}")