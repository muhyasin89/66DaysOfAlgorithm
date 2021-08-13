import json

arr = [
    {
        "room_id": 165,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "a1 test 1 repair and maintenance by owner",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 164,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "a2 test 1 vacant dirty",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 172,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "a",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 173,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "c",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 174,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "d",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 161,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "d test 1 temporary occupied",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "temporary",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 160,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "f test 1 on transformation",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "renovation",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 159,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "2fest 1 repair and maintenance",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 175,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "g",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 180,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "ini astaga 1",
        "room_variant_name": "astaga",
        "room_price": 2500000,
        "room_original_price": 2500000,
        "room_discount": 0.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 181,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "ini astaga 2",
        "room_variant_name": "astaga",
        "room_price": 2500000,
        "room_original_price": 2500000,
        "room_discount": 0.0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 182,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "ini astaga 3",
        "room_variant_name": "astaga",
        "room_price": 2500000,
        "room_original_price": 2500000,
        "room_discount": 0.0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 176,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "old cheap 1",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 177,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "old cheap 2",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 184,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "paket wew2",
        "room_variant_name": "ada apa wew",
        "room_price": 400000.0,
        "room_original_price": 500000,
        "room_discount": 100000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 185,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "paket wew3",
        "room_variant_name": "ada apa wew",
        "room_price": 400000.0,
        "room_original_price": 500000,
        "room_discount": 100000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 183,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "paket wew",
        "room_variant_name": "ada apa wew",
        "room_price": 400000.0,
        "room_original_price": 500000,
        "room_discount": 100000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 178,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "r-123",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 179,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "r-124",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 158,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "2test 1 rooms",
        "room_variant_name": "test 1",
        "room_price": 2000000.0,
        "room_original_price": 4000000,
        "room_discount": 2000000.0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 157,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "this is name",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 166,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "1",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "renovation",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 167,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "2",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "temporary",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 168,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "3",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 169,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "10",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "repair",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 170,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "13",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
    {
        "room_id": 171,
        "room_check_in_date": " - ",
        "room_check_out_date": " - ",
        "room_name": "15",
        "room_variant_name": "Lagi lagi",
        "room_price": 3000000,
        "room_original_price": 3000000,
        "room_discount": 0,
        "room_status": "available",
        "room_tenant_name": " - ",
    },
]


class Position:
    def __init__(self, val=0):
        self.val = val


def quickSort(start, end, arr):

    n = len(arr)

    start = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    left = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    right = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    mid = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    end = Position(end.val) if isinstance(end, Position) else Position(end)

    if start.val > end.val:
        return
    pivot = Position(arr[end.val])

    if start.val < 0 or start.val >= n or end.val < 0 or end.val >= n:
        raise AssertionError

    while right.val != end.val:

        if int(arr[right.val]["room_price"]) < int(pivot.val["room_price"]):
            # left, right
            arr[left.val], arr[right.val] = arr[right.val], arr[left.val]
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
            left.val += 1
            right.val += 1
            mid.val += 1
        elif int(arr[right.val]["room_price"]) == int(pivot.val["room_price"]):
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
            mid.val += 1
            right.val += 1
        elif int(arr[right.val]["room_price"]) > int(pivot.val["room_price"]):
            right.val += 1

        # mid, right
        arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
        start = start if isinstance(start, Position) else Position(start)
        left = left if isinstance(left, Position) else Position(left)
        mid = mid if isinstance(mid, Position) else Position(mid)
        end = end if isinstance(end, Position) else Position(end)

        quickSort(start.val, left.val - 1, arr)
        quickSort(mid.val + 1, end.val, arr)


quickSort(0, len(arr) - 1, arr)


def printArr(arr):
    for item in arr:
        print("{} -> ".format(item["room_price"]), end=" ")

    print("\n")


printArr(arr)
