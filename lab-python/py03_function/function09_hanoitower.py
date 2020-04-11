def hanoi_tower(n, start, target, aux):
    """
    재귀 함수를 이용한 하노이 타워

    :param n: 옮길 원반의 개수(양의 정수)
    :param start: 시작 기둥의 번호. n개의 원반이 처음에 있었던 위치.
    :param target: 원반들을 모두 옮겨 놓을 타겟 기둥의 번호.
    :param aux: 원반들을 옮길 때 보조 기둥으로 사용할 기둥의 번호.
    :return: None
    """

    # 원반이 한개만 있으면, 시작 위치에서 target 위치로 옮기고 종료함.
    if n == 1:
        print(f'{start} -> {target}')
        return  # 재귀 함수를 종료하기 위해서
        # return 문에 아무 값이 없으면 return None과 동일

    # (n-1)개의 원반을 start 위치에서 aux 위치로 옮김.
    hanoi_tower(n-1, start, aux, target)

    # 시작 기둥에 남아 있는 마지막 1개의 원반을 target 위치로 옮김.
    print(f'{start} -> {target}')

    # 보조 기둥에 있는 (n-1)개의 원반을 target 위치로 옮김.
    hanoi_tower(n-1, aux, target, start)


hanoi_tower(n=3, start=1, target=3, aux=2)
