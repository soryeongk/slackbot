def answer(text):
    if "소령" in text:
        reply = ":dait_happy: : 넴"
    elif 'UBDCWMFND' in text:
        reply = "이제부터 @ahlum cho님을 따라다녀요 :dait_happy:"
    elif 'UBDN90RJQ' in text:
        reply = "@miningful님 방토는여? :angry:"
    elif '짬뽕' in text:
        reply = "짬뽕?! :soso:"
    elif 'UBDRWU3GT' in text:
        reply = "차가운 예원님.. :sob:"
    elif "주사위" == text:
        die = str(random.randint(1, 6))
    else:
        reply = 'None'

    return reply
