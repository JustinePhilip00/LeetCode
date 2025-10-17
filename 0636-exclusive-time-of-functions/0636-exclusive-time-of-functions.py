class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0]*n;
        call_stack =[];
        prev_end = 0;
        for log in logs:
            fid, call_type, tstamp = log.split(":");
            fid = int(fid);
            tstamp = int(tstamp);
            if call_type=="start":
                if call_stack:
                    output[call_stack[-1]] = output[call_stack[-1]]+tstamp - prev_end;
                call_stack.append(fid);
                prev_end = tstamp; 
            else:
                output[call_stack.pop()] += (tstamp + 1) - prev_end;
                prev_end = tstamp+1;
        return output;
            
