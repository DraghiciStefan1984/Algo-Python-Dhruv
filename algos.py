def binary_search(lst, i):
    first=0
    last=len(lst)
    found=False
    j=len(lst)

    while(not found):
        mid=(first+last)//2
        if lst[mid]==i:
            return mid
        elif lst[mid]<i:
            last=mid+1
        elif lst[mid]>i:
            last=mid-1
        j-=1
        if j<=0:
            found=True


def insertion_sort(lst):
    for i in range(0, len(lst)):
        j=i+1
        done=False
        while j>=0 and not done:
            if lst[i]<lst[j]:
                lst[i], lst[j]=lst[j], lst[i]
            else:
                done=True
            j-=1


def selection_sort(lst):
    for i in range(0, len(lst)-1):
        smallest=-1
        index=0
        for j in range(i, len(lst)-1):
            smallest=lst[j]
            index=j
        num=lst[i]
        lst[i]=smallest
        lst[index]=num
