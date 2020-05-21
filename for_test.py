def triangles(n):
    p = [1]
    sum = 0
    while n-1:
         # generator函数与普通函数的差别：在执行过程中，遇到yield就中断，下次又继续执行
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]
        print('-----',p)
        for j in range(len(p)):
            if p[j] > 1:
                print('ppp', p[j])
                for k in range(2, p[j]+1):
                    print('--for in',k)
                    if p[j] == 2:
                        sum += p[j]
                        break
                    elif (p[j] % k) == 0:
                        print(p[j], "不是质数")
                        print(p[j], "乘于", p[j] // k, "是", p[j])
                        break
                    else:
                        sum += p[j]
                        print(p[j], "是质数")
                        break
            print('--此时的sum',sum)
            # 如果输入的数字小于或等于 1，不是质数

        n -= 1
    print(sum)

triangles(6)
