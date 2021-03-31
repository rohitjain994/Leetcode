class Solution:
    def trap(self, height: List[int]) -> int:
        #Binary Search 
        n = len(height)
        if n==0:return 0
        i=mi=me=res=0
        e=n-1
        while i<=e:
            if height[i]<height[e]:
                mi = max(height[i],mi)
                res+=mi-height[i]
                i+=1
            else:
                me = max(height[e],me)
                res+=me-height[e]
                e-=1
        return res
        # #2 array space(o(N))
        # n = len(height)
        # if n==0: return 0
        # lmax = [0]*n
        # lmax[0] = height[0]
        # for i in range(1,n):
        #     lmax[i] = max(lmax[i-1],height[i])
        # rmax = [0]*n
        # rmax[n-1] = height[n-1]
        # for i in range(n-2,-1,-1):
        #     rmax[i] = max(rmax[i+1],height[i])
        # cnt = 0
        # for i in range(1,n-1):
        #     cnt+=min(rmax[i],lmax[i])-height[i]
        # return cnt
