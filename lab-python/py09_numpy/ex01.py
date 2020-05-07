def add_vector(v1, v2):
    """길이가 같은 두개의 list를 전달받아서,
    원소별(element-wise)로 각각 더한 값들의 list를 리턴"""
    if len(v1) != len(v2):
        raise ValueError('add_vector(v1, v2)에서 v1, v2는 같은 길이여야 함!')

    n = len(v1)  # v1의 원소의 개수
    # result = []
    # for i in range(n):
    #     result.append(v1[i] + v2[i])
    result = [v1[i] + v2[i] for i in range(n)]
    return result


def add_vector2(v1, v2):
    if len(v1) != len(v2):
        raise ValueError('add_vector(v1, v2)에서 v1, v2는 같은 길이여야 함!')
    return [x + y for x, y in zip(v1, v2)]


def vector_dot(v1, v2):
    if len(v1) != len(v2):
        raise ValueError('add_vector(v1, v2)에서 v1, v2는 같은 길이여야 함!')
    # total = 0
    # for i in range(len(v1)):
    #     total += v1[i] * v2[i]
    # return total

    return sum(x * y for x, y in zip(v1, v2))


def scalar_multiply(vector, n):
    """리스트 vector의 모든 원소에 곱하기 n을 한 결과를 리스트로 리턴"""
    return [x * n for x in vector]


if __name__ == '__main__':
    # list 복습
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]

    result = nums1 + nums2
    # list에서 + 연산은 두 개의 리스트를 이어주는 기능(concatenate)
    print(result)

    # result = nums1 - nums2
    # list에서 - 연산은 정의되어 있지 않음.

    result = add_vector(nums1, nums2)
    print(result)  # [5, 7, 9]

    result = add_vector([1,2,3,4,5], [1,1,1,1,1])
    print(result)

    result = add_vector2(nums1, nums2)
    print(result)

    result = vector_dot(nums1, nums2)
    print(result)  # 1*4 + 2*5 + 3*6

    print(nums1 * 2)  # [1, 2, 3] * 2
    # list의 * 연산은 모든 연산을 곱하는 숫자만큼 반복하는 기능

    result = scalar_multiply(nums1, 2)
    print(result)  # [2, 4, 6]
