def rotate_array(nums,k):
    n = len(nums)
    k = k % n
    nums.reverse()
    nums[:k]=reversed(nums [:k])
    nums[k:]=reversed(nums [k:])

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int,input().split()))
    k = int(input())

    rotate_array(nums,k)
    print(" ".join(map(str,nums)))