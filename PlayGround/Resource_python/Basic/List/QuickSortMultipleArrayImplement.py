import json

NISSAN = "Nissan"
TOYOTA = "Toyota"
MITSUBISI = "Mitsubisi"
TESLA = "Tesla"

AVAILABLE = "Available"
MODIF = "Modif"

arr = [
    {
        "mobil_id": 165,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "Toyota Bapuk",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 164,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "Entah",
        "mobil_variant_name": NISSAN,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 172,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "Entah Mobil",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 173,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "c",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 174,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "d",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 161,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "tesla dari mana",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": "temporary",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 160,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "f test 1 on transformation",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": MODIF,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 159,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "2fest 1 repair and maintenance",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 175,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "g",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 180,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "ini astaga 1",
        "mobil_variant_name": MITSUBISI,
        "mobil_price": 2500000,
        "mobil_original_price": 2500000,
        "mobil_discount": 0.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 181,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "ini astaga 2",
        "mobil_variant_name": MITSUBISI,
        "mobil_price": 2500000,
        "mobil_original_price": 2500000,
        "mobil_discount": 0.0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 182,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "ini astaga 3",
        "mobil_variant_name": MITSUBISI,
        "mobil_price": 2500000,
        "mobil_original_price": 2500000,
        "mobil_discount": 0.0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 176,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "old cheap 1",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 177,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "old cheap 2",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 184,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "paket wew2",
        "mobil_variant_name": TOYOTA,
        "mobil_price": 400000.0,
        "mobil_original_price": 500000,
        "mobil_discount": 100000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 185,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "paket wew3",
        "mobil_variant_name": TOYOTA,
        "mobil_price": 400000.0,
        "mobil_original_price": 500000,
        "mobil_discount": 100000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 183,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "paket wew",
        "mobil_variant_name": TOYOTA,
        "mobil_price": 400000.0,
        "mobil_original_price": 500000,
        "mobil_discount": 100000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 178,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "r-123",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 179,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "r-124",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 158,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "2test 1 rooms",
        "mobil_variant_name": TESLA,
        "mobil_price": 2000000.0,
        "mobil_original_price": 4000000,
        "mobil_discount": 2000000.0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 157,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "this is name",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 166,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "1",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": MODIF,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 167,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "2",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": "temporary",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 168,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "3",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 169,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "10",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": "repair",
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 170,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "13",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
    {
        "mobil_id": 171,
        "mobil_sell_date": " - ",
        "mobil_purchase_out_date": " - ",
        "mobil_name": "15",
        "mobil_variant_name": NISSAN,
        "mobil_price": 3000000,
        "mobil_original_price": 3000000,
        "mobil_discount": 0,
        "mobil_status": AVAILABLE,
        "mobil_tenant_name": " - ",
        "applied_discount": False,
    },
]


class Position:
    def __init__(self, val=0):
        self.val = val


def change_to_position(pos, initial=True):
    if initial:
        return Position(pos.val) if isinstance(pos, Position) else Position(pos)
    else:
        return pos if isinstance(pos, Position) else Position(pos)


def quickSort(start, end, arr):

    n = len(arr)

    start = change_to_position(start)
    left = change_to_position(start)
    right = change_to_position(start)
    mid = change_to_position(start)
    end = change_to_position(end)

    if start.val > end.val:
        return
    pivot = Position(arr[end.val])

    if start.val < 0 or start.val >= n or end.val < 0 or end.val >= n:
        raise AssertionError

    while right.val != end.val:

        if int(arr[right.val]["mobil_price"]) < int(pivot.val["mobil_price"]):
            # left, right
            arr[left.val], arr[right.val] = arr[right.val], arr[left.val]
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
            left.val += 1
            right.val += 1
            mid.val += 1
        elif int(arr[right.val]["mobil_price"]) == int(
            pivot.val["mobil_price"]
        ):
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]

            mid.val += 1
            right.val += 1
        elif int(arr[right.val]["mobil_price"]) > int(pivot.val["mobil_price"]):
            right.val += 1

        # mid, right
        arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]

        start = change_to_position(start, False)
        left = change_to_position(left, False)
        mid = change_to_position(mid, False)
        end = change_to_position(end, False)

        quickSort(start.val, left.val - 1, arr)
        quickSort(mid.val + 1, end.val, arr)

    return arr


def printArr(arr):
    for item in arr:
        print("{} -> ".format(item["mobil_price"]), end=" ")

    print("\n")


printArr(quickSort(0, len(arr) - 1, arr))
