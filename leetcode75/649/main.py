from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dQ = deque()
        rQ = deque()

        for i in range(len(senate)):
            if senate[i] == "D":
                dQ.append(i)
            elif senate[i] == "R":
                rQ.append(i)

        while dQ and rQ:
            d_idx = dQ.popleft()
            r_idx = rQ.popleft()

            if d_idx < r_idx:
                dQ.append(d_idx + len(senate))
            else:
                rQ.append(r_idx + len(senate))

        if dQ:
            return "Dire"
        else:
            return "Radiant"
