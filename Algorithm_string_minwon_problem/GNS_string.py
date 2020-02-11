numbers = int(input())

for number in range(numbers):
    problem_num, problem_len = list(map(str, input().split()))
    GNS = list(map(str, input().split()))

    ZRO_count = GNS.count('ZRO')
    ONE_count = GNS.count('ONE')
    TWO_count = GNS.count('TWO')
    THR_count = GNS.count('THR')
    FOR_count = GNS.count('FOR')
    FIV_count = GNS.count('FIV')
    SIX_count = GNS.count('SIX')
    SVN_count = GNS.count('SVN')
    EGT_count = GNS.count('EGT')
    NIN_count = GNS.count('NIN')

    GNS_result = []

    for i in range(ZRO_count):
        GNS_result.append('ZRO')

    for i in range(ONE_count):
        GNS_result.append('ONE')

    for i in range(TWO_count):
        GNS_result.append('TWO')

    for i in range(THR_count):
        GNS_result.append('THR')

    for i in range(FOR_count):
        GNS_result.append('FOR')

    for i in range(FIV_count):
        GNS_result.append('FIV')

    for i in range(SIX_count):
        GNS_result.append('SIX')

    for i in range(SVN_count):
        GNS_result.append('SVN')

    for i in range(EGT_count):
        GNS_result.append('EGT')

    for i in range(NIN_count):
        GNS_result.append('NIN')

    print(problem_num)
    print(*GNS_result)