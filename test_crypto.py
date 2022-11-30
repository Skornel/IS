from symmetric.gost import gost2015
from publickey.ec import ECPoint
from publickey.gost import DSGOST
import binascii

def test_gost_sign():
    p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)
    key = 55441196065363246126355624130324183196576709222340016572108097750006097525544
    message = 20798893674476452017134061561508270130637142515379653289952617252661468872421
    k = 53854137677348463731403841147996619241504003434302020712960838528893196233395
    sign = gost.sign(message, key, k)
    expected = (29700980915817952874371204983938256990422752107994319651632687982059210933395,
                574973400270084654178925310019147038455227042649098563933718999175515839552)
    print ("Сгенерированная подпись: ", sign, "\nТребуемая: ", expected)
    assert sign == expected, 'Сгенерированная подпись не равна представленной'


def test_gost_verify():
    p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580414
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)
    message = 20798893674476452017134061561508270130637142515379653289952617252661468872421
    sign = (29700980915817952874371204983938256990422752107994319651632687982059210933395,
            574973400270084654178925310019147038455227042649098563933718999175515839552)
    q_x = 57520216126176808443631405023338071176630104906313632182896741342206604859403
    q_y = 17614944419213781543809391949654080031942662045363639260709847859438286763994
    public_key = ECPoint(q_x, q_y, a, b, p)
    if(gost.verify(message, sign, public_key) == True): print ("Верификация пройдена")

def Error_test_gost_sign():
    p = 5789604461865809771178549224343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580415
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)
    key = 55441196065363246126355624130324183196576709222340016572108097750006097525544
    message = 20798893674476452017134061561508270130637142515379653289952617252661468872421
    k = 53854137677348463731403841147996619241504003434302020712960838528893196233395
    sign = gost.sign(message, key, k)
    expected = (29700980915817952874371204983938256990422752107994319651632687982059210933395,
                574973400270084654178925310019147038455227042649098563933718999175515839552)
    print ("Сгенерированная подпись: ", sign, "\nТребуемая: ", expected)
    


def Error_test_gost_verify():
    p = 57896044618658097711785492504343953926634992332820282019728792003956564821041
    a = 7
    b = 43308876546767276905765904595650931995942111794451039583252968842033849580413
    x = 2
    y = 4018974056539037503335449422937059775635739389905545080690979365213431566280
    q = 57896044618658097711785492504343953927082934583725450622380973592137631069619
    gost = DSGOST(p, a, b, q, x, y)
    message = 20798893674476452017134061561508270130637142515379653289952617252661468872421
    sign = (2970098091581795287437120498393822990422752107994319651632687982059210933395,
            574973400270084654178925310019147038455227042649098563933718999175515839552)
    q_x = 57520216126176808443631405023338071176630104906313632182896741342206604859403
    q_y = 17614944419213781543809391949654080031942662045363639260709847859438286763994
    public_key = ECPoint(q_x, q_y, a, b, p)
    if (gost.verify(message, sign, public_key) != True): print("\nВерификация не пройдена")

print ("\tКорректная подпись: \n")
test_gost_sign()
test_gost_verify()

print ("\n\tНекорректная подпись: \n")
Error_test_gost_sign()
Error_test_gost_verify()

input()


