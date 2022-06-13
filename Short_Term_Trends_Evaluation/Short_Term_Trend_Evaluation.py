# coding=utf-8
# accuracy = TP / TP + FP
# Intersects with actual / Intersect with actual + (Intersect with actual - length of predicted)

TH = 0.3

def accuracy_unigram_keyword_accuracy():
    print("---------------------------Keyword Accuracy Calculating(Unigram)-------------------------")
    print("")
    # 25
    A1 = ['උළෙලේ', 'සෞඛ්යය', 'කිරීම', 'භානුක', 'මිල්කා', 'වූ']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['අමාත්යවරයා', 'උනා']
    pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
    A1_2 = ['එකේ', 'වාර්තා', 'කරයි']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['කෙනෙක්', 'කිව්වතරුණයෙක්', 'කිව්ව', 'ලැජ්ජ', 'වෙන්න', 'ඕනෙ']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['ක්රීඩා කරන කෙනෙක් අමාත්යවරයා උනා කිව්වතරුණයෙක් ක්රීඩා අමාත්යවරයා උනා කිව්ව ලැජ්ජ වෙන්න ඕනෙ']
    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))

    acc1 = len(set(pre1).intersection(set(act1))) / (
            len(set(pre1).intersection(set(act1))) + (len(set(pre1).symmetric_difference(set(act1)))))
    acc1_1 = len(set(pre1_1).intersection(set(act1))) / (
            len(set(pre1_1).intersection(set(act1))) + (len(set(pre1_1).symmetric_difference(set(act1)))))
    acc1_2 = len(set(pre1_2).intersection(set(act1))) / (
            len(set(pre1_2).intersection(set(act1))) + (len(set(pre1_2).symmetric_difference(set(act1)))))
    acc1_3 = len(set(pre1_3).intersection(set(act1))) / (
            len(set(pre1_3).intersection(set(act1))) + (len(set(pre1_3).symmetric_difference(set(act1)))))
    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3) / 4

    # 26
    A2 = ['ඔලිම්පික්', 'වූ']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['නැති', 'කමද']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['ක්රීඩා']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['උළෙලට', 'සහභාගී', 'නිලූක', 'කරුණාරත්න', 'චාමර', 'නුවන්', 'බිමට']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['ඔලිම්පික් ක්රීඩා උළෙලට සහභාගී වූ නිලූක කරුණාරත්න චාමර නුවන් තරඟ බිමට']
    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))

    acc2 = len(set(pre2).intersection(set(act2))) / (
            len(set(pre2).intersection(set(act2))) + (len(set(pre2).symmetric_difference(set(act2)))))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) / (
            len(set(pre2_1).intersection(set(act2))) + (len(set(pre2_1).symmetric_difference(set(act2)))))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) / (
            len(set(pre2_2).intersection(set(act2))) + (len(set(pre2_2).symmetric_difference(set(act2)))))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) / (
            len(set(pre2_3).intersection(set(act2))) + (len(set(pre2_3).symmetric_difference(set(act2)))))

    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # print("----------Done untill Here----------")
    # print("Accuracyyyyyy ",acc2)
    # 27
    A3 = ['ලැබු', 'ප්රතිඵලය', 'සතුටුට', 'පත්', 'නොවන', 'අතින්', 'උපාය', 'මාර්ගික', 'වරදක්', 'සිදුවු', 'පවසනව', 'ජය', 'පරාජය', 'තම', 'දිවිය', 'පරාජයන්', 'අත්විද', 'පිහිණුම්', 'දක්ෂ', 'ප්රකාශ']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['ක්රීඩාවේ']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['වගේම']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['මැතිව්', 'අබේසිංහ']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['ලැබු ප්රතිඵලය තමන් සතුටුට පත් නොවන තමන් අතින් උපාය මාර්ගික වරදක් සිදුවු මැතිව් අබේසිංහ පවසනව ජය පරාජය ක්රීඩාවේ අංගය තම ක්රීඩා දිවිය ජයග්රහණ වගේම පරාජයන් තමන් අත්විද පිහිණුම් දක්ෂ මැතිව් අබේසිංහ ප්රකාශ කළා']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))

    acc3 = len(set(pre1).intersection(set(act3))) / (
            len(set(pre1).intersection(set(act3))) + (len(set(pre1).symmetric_difference(set(act3)))))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) / (
            len(set(pre3_1).intersection(set(act3))) + (len(set(pre3_1).symmetric_difference(set(act3)))))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) / (
            len(set(pre3_2).intersection(set(act3))) + (len(set(pre3_2).symmetric_difference(set(act3)))))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) / (
            len(set(pre3_3).intersection(set(act3))) + (len(set(pre3_3).symmetric_difference(set(act3)))))

    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    # 28
    A4 = ['ලෝකඩ']
    pre4 = list(dict.fromkeys(w for s in A4 for w in s.split()))
    A4_1 = ['රිදී']
    pre4_1 = list(dict.fromkeys(w for s in A4_1 for w in s.split()))
    A4_2 = ['ඉසව්', 'ලංකාව', 'ජපාන', 'කොඩිය', 'සටහනේ', 'ස්ථානයට', 'පැමිණීමට', 'සත්කාරක', 'සමත්', 'පාණ්ඩ්යො']
    pre4_2 = list(dict.fromkeys(w for s in A4_2 for w in s.split()))
    A4_3 = ['පදක්කම්']
    pre4_3 = list(dict.fromkeys(w for s in A4_3 for w in s.split()))
    B4 = ['දශක ගණනාවක් තිස්සේ පිහිනුම් ඉසව් වලදී පිරිමින් පමණක වැඩිදුර තරග නිර්දේශවූ ඔලිම්පික් ක්රීඩා උළෙලේදී මීටර දුර නිදහස් ආර පිහිනීමට කාන්තාවන්ට ලබාදුන් ප්රථම අවස්ථාව මෙවර ටෝකියෝ ඔලිම්පික් උළෙලේදී සිදුවිය එහි අවසන් තරඟ අද පැවති කේටි ලෙඩෙක්']
    act4 = list(dict.fromkeys(w for s in B4 for w in s.split()))

    acc4 = len(set(pre4).intersection(set(act4))) / (
            len(set(pre4).intersection(set(act4))) + (len(set(pre4).symmetric_difference(set(act4)))))
    acc4_1 = len(set(pre4_1).intersection(set(act4))) / (
            len(set(pre4_1).intersection(set(act4))) + (len(set(pre4_1).symmetric_difference(set(act4)))))
    acc4_2 = len(set(pre4_2).intersection(set(act4))) / (
            len(set(pre4_2).intersection(set(act4))) + (len(set(pre4_2).symmetric_difference(set(act4)))))
    acc4_3 = len(set(pre4_3).intersection(set(act4))) / (
            len(set(pre4_3).intersection(set(act4))) + (len(set(pre4_3).symmetric_difference(set(act4)))))

    acc4 = (acc4 + acc4_1 + acc4_2 + acc4_3) / 4

    # print("Accuracyyyyyy ", acc4)
    # 29
    A5 = ['එදා', 'ලෝක', 'වැඩක්']
    pre5 = list(dict.fromkeys(w for s in A5 for w in s.split()))
    A5_1 = ['මලල']
    pre5_1 = list(dict.fromkeys(w for s in A5_1 for w in s.split()))
    A5_2 = ['ක්රීඩා', 'මෙවර', 'ජූලි', 'බලාපොරොත්තු', 'නිළ']
    pre5_2 = list(dict.fromkeys(w for s in A5_2 for w in s.split()))
    A5_3 = ['කණ්ඩාය', 'නිරෝධායනයට']
    pre5_3 = list(dict.fromkeys(w for s in A5_3 for w in s.split()))
    B5 = ['ඔස්ට්රේලියානු ඔලිම්පික් කණ්ඩාය නිරෝධායනයට මෙවර ඔලිම්පික් උළෙල සහභාගී ඔස්ට්රේලියානු මලල ක්රීඩා කණ්ඩාය නිරෝධායනයට යොමුකර තිබේ විස්තර']
    act5 = list(dict.fromkeys(w for s in B5 for w in s.split()))

    acc5 = len(set(pre5).intersection(set(act5))) / (
            len(set(pre5).intersection(set(act5))) + (len(set(pre5).symmetric_difference(set(act5)))))
    acc5_1 = len(set(pre5_1).intersection(set(act5))) / (
            len(set(pre5_1).intersection(set(act5))) + (len(set(pre5_1).symmetric_difference(set(act5)))))
    acc5_2 = len(set(pre5_2).intersection(set(act5))) / (
            len(set(pre5_2).intersection(set(act5))) + (len(set(pre5_2).symmetric_difference(set(act5)))))
    acc5_3 = len(set(pre5_3).intersection(set(act5))) / (
            len(set(pre5_3).intersection(set(act5))) + (len(set(pre5_3).symmetric_difference(set(act5)))))

    acc5 = (acc5 + acc5_1 + acc5_2 + acc5_3) / 4

    # print("Accuracyyyyyy ", acc5)
    # 30
    A6 = ['රාජපක්ෂ']
    pre6 = list(dict.fromkeys(w for s in A6 for w in s.split()))
    A6_1 = ['තරඟ', 'කරන', 'අමාත්යවරයා', 'ඉසව්', 'වූ', 'අවසන්', 'කර', 'ටෝකියෝ', 'ජාතික', 'ජය', 'එහි']
    pre6_1 = list(dict.fromkeys(w for s in A6_1 for w in s.split()))
    A6_2 = ['ක්රීඩා', 'මලල', 'නිමාලි', 'කාටත', 'පුලුවන්']
    pre6_2 = list(dict.fromkeys(w for s in A6_2 for w in s.split()))
    # A6_3 = ['භානුක', 'රාජපක්ෂ', 'හට', 'අවසන්', 'පන්දු', 'වාර', 'තරඟ', 'දෙකත්', 'අහිමි', 'ලකුණු', 'ලෝකෙ', 'රෙදි', 'මහන',
    #         'රටකට', 'ඔලිම්පික්', 'කණ්ඩායමට', 'ඒඒ', 'ක්රීඩාවට', 'අදාලව', 'ජාතික', 'ක්රීඩා', 'ඇදුම', 'සපයගන්න', 'බැරි',
    #         'වුවමනා', 'නැති', 'කමද', 'ගාණක්']
    # pre6_3 = list(dict.fromkeys(w for s in A6_3 for w in s.split()))
    B6 = ['කඟවේණුන්ගේ ජවය උරගා බැලෙන ඔලිම්පික් මලල ක්රීඩා වසන්තය ඇරඹේ']
    act6 = list(dict.fromkeys(w for s in B6 for w in s.split()))

    acc6 = len(set(pre6).intersection(set(act6))) / (
            len(set(pre6).intersection(set(act6))) + (len(set(pre6).symmetric_difference(set(act6)))))
    acc6_1 = len(set(pre6_1).intersection(set(act6))) / (
            len(set(pre6_1).intersection(set(act6))) + (len(set(pre6_1).symmetric_difference(set(act6)))))
    acc6_2 = len(set(pre6_2).intersection(set(act6))) / (
            len(set(pre6_2).intersection(set(act6))) + (len(set(pre6_2).symmetric_difference(set(act6)))))

    TP = 0
    FP = 0
    TH = 0.20

    if acc1 >= TH:
        TP = TP + 1
    elif acc1 < TH:
        FP = FP + 1

    if acc1_1 >= TH:
        TP = TP + 1
    elif acc1_1 < TH:
        FP = FP + 1

    if acc1_2 >= TH:
        TP = TP + 1
    elif acc1_2 < TH:
        FP = FP + 1

    if acc1_3 >= TH:
        TP = TP + 1
    elif acc1_3 < TH:
        FP = FP + 1

    if acc2 >= TH:
        TP = TP + 1
    elif acc2 < TH:
        FP = FP + 1

    if acc2_1 >= TH:
        TP = TP + 1
    elif acc2_1 < TH:
        FP = FP + 1

    if acc2_2 >= TH:
        TP = TP + 1
    elif acc2_2 < TH:
        FP = FP + 1

    if acc2_3 >= TH:
        TP = TP + 1
    elif acc2_3 < TH:
        FP = FP + 1

    if acc3 >= TH:
        TP = TP + 1
    elif acc3_1 < TH:
        FP = FP + 1

    if acc3_2 >= TH:
        TP = TP + 1
    elif acc3_2 < TH:
        FP = FP + 1

    if acc3_3 >= TH:
        TP = TP + 1
    elif acc3_3 < TH:
        FP = FP + 1

    if acc4 >= TH:
        TP = TP + 1
    elif acc4 < TH:
        FP = FP + 1

    if acc4_1 >= TH:
        TP = TP + 1
    elif acc4_1 < TH:
        FP = FP + 1

    if acc4_2 >= TH:
        TP = TP + 1
    elif acc4_2 < TH:
        FP = FP + 1

    if acc4_3 >= TH:
        TP = TP + 1
    elif acc4_3 < TH:
        FP = FP + 1

    if acc5 >= TH:
        TP = TP + 1
    elif acc5 < TH:
        FP = FP + 1

    if acc5_1 >= TH:
        TP = TP + 1
    elif acc5_1 < TH:
        FP = FP + 1

    if acc5_2 >= TH:
        TP = TP + 1
    elif acc5_2 < TH:
        FP = FP + 1

    if acc5_3 >= TH:
        TP = TP + 1
    elif acc5_3 < TH:
        FP = FP + 1

    if acc6 >= TH:
        TP = TP + 1
    elif acc6 < TH:
        FP = FP + 1

    if acc6_1 >= TH:
        TP = TP + 1
    elif acc6_1 < TH:
        FP = FP + 1

    if acc6_2 >= TH:
        TP = TP + 1
    elif acc6_2 < TH:
        FP = FP + 1


    UPrecision = (TP / (TP + FP))


    print("Overall Precision for Unigram ::::::", UPrecision)


# coding=utf-8

# def accuracy_bigram_keyword_accuracy():
#     print("---------------------------Keyword Accuracy Calculating(bigram)-------------------------")
#     print(" ")
#     # 25
#     A1 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේ', 'භානුක', 'රාජපක්ෂ']
#     pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
#     A1_1 = ['අමාත්යවරයා', 'උනා']
#     pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
#     A1_2 = ['ඕනෙ', 'ක්රීඩා']
#     pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
#     A1_3 = ['ක්රීඩා', 'කරන', 'කෙනෙක්', 'අමාත්යවරයා', 'උනා', 'කිව්වතරුණයෙක්', 'කිව්ව', 'ලැජ්ජ', 'වෙන්න', 'ඕනෙ']
#     pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
#     B1 = ['ක්රීඩා කරන කෙනෙක් අමාත්යවරයා උනා කිව්වතරුණයෙක් ක්රීඩා අමාත්යවරයා උනා කිව්ව ලැජ්ජ වෙන්න ඕනෙ']
#     act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))
#     acc1 = len(set(pre1).intersection(set(act1))) * len(set(pre1).intersection(set(act1)))/(len(pre1) * len(act1))
#     acc1_1 = len(set(pre1_1).intersection(set(act1))) * len(set(pre1_1).intersection(set(act1)))/(len(pre1_1) * len(act1))
#     acc1_2 = len(set(pre1_2).intersection(set(act1))) * len(set(pre1_2).intersection(set(act1)))/(len(pre1_2) * len(act1))
#     acc1_3 = len(set(pre1_3).intersection(set(act1))) * len(set(pre1_3).intersection(set(act1)))/(len(pre1_3) * len(act1))
#     acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3)/4
#     # print("----",acc1)
#     # print("Predicted Keywords : ",repA)
#     # print("Actual Keywords : ",repB)
#     # print("length of actual = ", len(repB))
#     # print("length of predicted = ", len(repA))
#     # print("similar word count = ", len(set(repA).intersection(set(repB))))
#     # 26
#     A2 = ['බිමට', 'ඔලිම්පික්']
#     pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
#     A2_1 = ['ක්රීඩා', 'උළෙලට', 'සහභාගී', 'වූ', 'නිලූක', 'කරුණාරත්න', 'චාමර', 'නුවන්', 'තරඟ', 'බිමට']
#     pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
#     A2_2 = ['නැති', 'කමද']
#     pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
#     A2_3 = ['ඔලිම්පික්', 'ක්රීඩා']
#     pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
#     B2 = ['ඔලිම්පික් ක්රීඩා උළෙලට සහභාගී වූ නිලූක කරුණාරත්න චාමර නුවන් තරඟ බිමට']
#     act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))
#     acc2 = len(set(act2).intersection(set(pre2))) * len(set(act2).intersection(set(pre2))) / (len(act2) * len(pre2))
#     acc2_1 = len(set(pre2_1).intersection(set(act2))) * len(set(pre2_1).intersection(set(act2))) / (
#                 len(pre2_1) * len(act2))
#     acc2_2 = len(set(pre2_2).intersection(set(act2))) * len(set(pre2_2).intersection(set(act2))) / (
#             len(pre2_2) * len(act2))
#     acc2_3 = len(set(pre2_3).intersection(set(act2))) * len(set(pre2_3).intersection(set(act2))) / (
#             len(pre2_3) * len(act2))
#     acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4
#
#     # print("----------Done untill Here----------")
#     # print("Accuracyyyyyy ",acc2)
#     # 27
#     A3 = ['පැවැත්වී', 'නියමිත', 'ක්රීඩා', 'උළෙලේ', 'භානුක', 'රාජපක්ෂ', 'තරඟ']
#     pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
#     A3_1 = ['ඔලිම්පික්', 'ක්රීඩා', 'අමාත්යවරයා']
#     pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
#     A3_2 = ['ලැබු', 'ප්රතිඵලය', 'තමන්', 'සතුටුට', 'පත්', 'නොවන', 'අතින්', 'උපාය', 'මාර්ගික', 'වරදක්', 'සිදුවු', 'මැතිව්', 'අබේසිංහ', 'පවසනව', 'ජය', 'පරාජය', 'ක්රීඩාවේ', 'අංගය', 'තම', 'ක්රීඩා', 'දිවිය', 'ජයග්රහණ', 'වගේම', 'පරාජයන්', 'අත්විද', 'පිහිණුම්', 'දක්ෂ', 'ප්රකාශ', 'කළා']
#     pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
#     A3_3 = ['මැතිව්', 'අබේසිංහ']
#     pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
#     B3 = ['ලැබු ප්රතිඵලය තමන් සතුටුට පත් නොවන තමන් අතින් උපාය මාර්ගික වරදක් සිදුවු මැතිව් අබේසිංහ පවසනව ජය පරාජය ක්රීඩාවේ අංගය තම ක්රීඩා දිවිය ජයග්රහණ වගේම පරාජයන් තමන් අත්විද පිහිණුම් දක්ෂ මැතිව් අබේසිංහ ප්රකාශ කළා']
#     act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))
#     acc3 = len(set(act3).intersection(set(pre3))) * len(set(act3).intersection(set(pre3))) / (len(act3) * len(pre3))
#     acc3_1 = len(set(pre3_1).intersection(set(act3))) * len(set(pre3_1).intersection(set(act3))) / (
#             len(pre3_1) * len(act3))
#     acc3_2 = len(set(pre3_2).intersection(set(act3))) * len(set(pre3_2).intersection(set(act3))) / (
#             len(pre3_2) * len(act3))
#     acc3_3 = len(set(pre3_3).intersection(set(act3))) * len(set(pre3_3).intersection(set(act3))) / (
#             len(pre3_3) * len(act3))
#     acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4
#
#     # print("Accuracyyyyyy ", acc3)
#     # 28
#     A4 = ['ලෝකඩ', 'පදක්කම්']
#     pre4 = list(dict.fromkeys(w for s in A4 for w in s.split()))
#     A4_1 = ['දශක', 'ගණනාවක්', 'තිස්සේ', 'පිහිනුම්', 'ඉසව්', 'වලදී', 'පිරිමින්', 'පමණක', 'වැඩිදුර', 'තරග', 'නිර්දේශවූ', 'ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේදී', 'මීටර', 'දුර', 'නිදහස්', 'ආර', 'පිහිනීමට', 'කාන්තාවන්ට', 'ලබාදුන්', 'ප්රථම', 'අවස්ථාව', 'මෙවර', 'ටෝකියෝ', 'සිදුවිය', 'එහි', 'අවසන්', 'තරඟ', 'අද', 'පැවති', 'කේටි', 'ලෙඩෙක්', 'උළෙලේ', 'පදක්කම්']
#     pre4_1 = list(dict.fromkeys(w for s in A4_1 for w in s.split()))
#     A4_2 = ['ක්රීඩා', 'අමාත්යවරයා']
#     pre4_2 = list(dict.fromkeys(w for s in A4_2 for w in s.split()))
#     A4_3 = ['ටෝකියෝ', 'ඔලිම්පික්', 'උළෙලේදී', 'ශ්රී', 'ලංකාව', 'ලෙඩෙක්', 'දශක', 'පදක්කම්', 'සටහනේ', 'පළමු', 'ස්ථානයට', 'පැමිණීමට', 'සත්කාරක', 'ජපාන', 'සමත්', 'තිබේ', 'රන්', 'රිදී', 'ලෝකඩ', 'දිනාගෙන', 'ඇත']
#     pre4_3 = list(dict.fromkeys(w for s in A4_3 for w in s.split()))
#     B4 = ['දශක ගණනාවක් තිස්සේ පිහිනුම් ඉසව් වලදී පිරිමින් පමණක වැඩිදුර තරග නිර්දේශවූ ඔලිම්පික් ක්රීඩා උළෙලේදී මීටර දුර නිදහස් ආර පිහිනීමට කාන්තාවන්ට ලබාදුන් ප්රථම අවස්ථාව මෙවර ටෝකියෝ ඔලිම්පික් උළෙලේදී සිදුවිය එහි අවසන් තරඟ අද පැවති කේටි ලෙඩෙක්']
#     act4 = list(dict.fromkeys(w for s in B4 for w in s.split()))
#     acc4 = len(set(act4).intersection(set(pre4))) * len(set(act4).intersection(set(pre4))) / (len(act4) * len(pre4))
#     acc4_1 = len(set(pre4_1).intersection(set(act4))) * len(set(pre4_1).intersection(set(act4))) / (
#             len(pre4_1) * len(act4))
#     acc4_2 = len(set(pre4_2).intersection(set(act4))) * len(set(pre4_2).intersection(set(act4))) / (
#             len(pre4_2) * len(act4))
#     acc4_3 = len(set(pre4_3).intersection(set(act4))) * len(set(pre4_3).intersection(set(act4))) / (
#             len(pre4_3) * len(act4))
#     acc4 = (acc4 + acc4_1 + acc4_2 + acc4_3) / 4
#
#     # print("Accuracyyyyyy ", acc4)
#     # 29
#     A5 = ['මලල', 'ක්රීඩා', 'කණ්ඩාය']
#     pre5 = list(dict.fromkeys(w for s in A5 for w in s.split()))
#     A5_1 = ['ඔලිම්පික්', 'උළෙල', 'විස්තර', 'ඔස්ට්රේලියානු']
#     pre5_1 = list(dict.fromkeys(w for s in A5_1 for w in s.split()))
#     A5_2 = ['කණ්ඩාය', 'නිරෝධායනයට']
#     pre5_2 = list(dict.fromkeys(w for s in A5_2 for w in s.split()))
#     A5_3 = ['මළල', 'ක්රීඩා', 'ඉතිහාසයේ', 'පිටුවක', 'ලියන', 'බලාපොරොත්තු', 'ඇතුව', 'ජූලි', 'ඔලිම්පික්', 'අපි', 'සල්ලි', 'දීල', 'තියෙන්න', 'ක්රීඩකයන්', 'නිළ', 'ඇඳුම්', 'දෙන', 'එක', 'කමිටුවෙ', 'වැඩක්', 'අධ්යක්ෂ', 'ජනරාල්']
#     pre5_3 = list(dict.fromkeys(w for s in A5_3 for w in s.split()))
#     B5 = ['ඔස්ට්රේලියානු ඔලිම්පික් කණ්ඩාය නිරෝධායනයට මෙවර ඔලිම්පික් උළෙල සහභාගී ඔස්ට්රේලියානු මලල ක්රීඩා කණ්ඩාය නිරෝධායනයට යොමුකර තිබේ විස්තර']
#     act5 = list(dict.fromkeys(w for s in B5 for w in s.split()))
#     acc5 = len(set(act5).intersection(set(pre5))) * len(set(act5).intersection(set(pre5))) / (len(act5) * len(pre5))
#     acc5_1 = len(set(pre5_1).intersection(set(act5))) * len(set(pre5_1).intersection(set(act5))) / (
#             len(pre5_1) * len(act5))
#     acc5_2 = len(set(pre5_2).intersection(set(act5))) * len(set(pre5_2).intersection(set(act5))) / (
#             len(pre5_2) * len(act5))
#     acc5_3 = len(set(pre5_3).intersection(set(act5))) * len(set(pre5_3).intersection(set(act5))) / (
#             len(pre5_3) * len(act5))
#     acc5 = (acc5 + acc5_1 + acc5_2 + acc5_3) / 4
#
#     # print("Accuracyyyyyy ", acc5)
#     # 30
#     A6 = ['රාජපක්ෂ', 'මැතිතුමා', 'ත්']
#     pre6 = list(dict.fromkeys(w for s in A6 for w in s.split()))
#     A6_1 = ['කාටත', 'පුලුවන්']
#     pre6_1 = list(dict.fromkeys(w for s in A6_1 for w in s.split()))
#     A6_2 = ['ක්රීඩා', 'අමාත්යවරයා', 'ඉසව්', 'ජාතික', 'ලෝලීන්']
#     pre6_2 = list(dict.fromkeys(w for s in A6_2 for w in s.split()))
#     # A6_3 = ['භානුක', 'රාජපක්ෂ', 'හට', 'අවසන්', 'පන්දු', 'වාර', 'තරඟ', 'දෙකත්', 'අහිමි', 'ලකුණු', 'ලෝකෙ', 'රෙදි', 'මහන',
#     #         'රටකට', 'ඔලිම්පික්', 'කණ්ඩායමට', 'ඒඒ', 'ක්රීඩාවට', 'අදාලව', 'ජාතික', 'ක්රීඩා', 'ඇදුම', 'සපයගන්න', 'බැරි',
#     #         'වුවමනා', 'නැති', 'කමද', 'ගාණක්']
#     # pre6_3 = list(dict.fromkeys(w for s in A6_3 for w in s.split()))
#     B6 = ['කඟවේණුන්ගේ ජවය උරගා බැලෙන ඔලිම්පික් මලල ක්රීඩා වසන්තය ඇරඹේ']
#     act6 = list(dict.fromkeys(w for s in B6 for w in s.split()))
#     acc6 = len(set(act6).intersection(set(pre6))) * len(set(act6).intersection(set(pre6))) / (len(act6) * len(pre6))
#     acc6_1 = len(set(pre6_1).intersection(set(act6))) * len(set(pre6_1).intersection(set(act6))) / (
#             len(pre6_1) * len(act6))
#     acc6_2 = len(set(pre6_2).intersection(set(act6))) * len(set(pre6_2).intersection(set(act6))) / (
#             len(pre6_2) * len(act6))
#     # acc6_3 = len(set(pre6_3).intersection(set(act6))) * len(set(pre6_3).intersection(set(act6))) / (
#     #         len(pre6_3) * len(act6))
#     acc6 = (acc6 + acc6_1 + acc6_2) / 3
#
#     # print("Accuracyyyyyy ", acc6)
#     print("Overall Accuracy for Bigram ::::::", (acc1+acc2+acc3+acc4+acc5+acc6)/6)



# coding=utf-8

def accuracy_bigram_keyword_accuracy():
    print("---------------------------Keyword Accuracy Calculating(bigram)-------------------------")
    print(" ")
    # 25
    A1 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේ', 'භානුක', 'රාජපක්ෂ']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['අමාත්යවරයා', 'උනා']
    pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
    A1_2 = ['ඕනෙ', 'ක්රීඩා']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['ක්රීඩා', 'කරන', 'කෙනෙක්', 'අමාත්යවරයා', 'උනා', 'කිව්වතරුණයෙක්', 'කිව්ව', 'ලැජ්ජ', 'වෙන්න', 'ඕනෙ']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['ක්රීඩා කරන කෙනෙක් අමාත්යවරයා උනා කිව්වතරුණයෙක් ක්රීඩා අමාත්යවරයා උනා කිව්ව ලැජ්ජ වෙන්න ඕනෙ']
    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))
    # acc1 = len(set(pre1).intersection(set(act1))) * len(set(pre1).intersection(set(act1)))/(len(pre1) * len(act1))

    acc1 = len(set(pre1).intersection(set(act1)))/(len(set(pre1).intersection(set(act1))) + (len(set(pre1).symmetric_difference(set(act1)))))
    acc1_1 = len(set(pre1_1).intersection(set(act1)))/(len(set(pre1_1).intersection(set(act1))) + (len(set(pre1_1).symmetric_difference(set(act1)))))
    acc1_2 = len(set(pre1_2).intersection(set(act1)))/(len(set(pre1_2).intersection(set(act1))) + (len(set(pre1_2).symmetric_difference(set(act1)))))
    acc1_3 = len(set(pre1_3).intersection(set(act1)))/(len(set(pre1_3).intersection(set(act1))) + (len(set(pre1_3).symmetric_difference(set(act1)))))
    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3)/4

    # print("---------1",acc1)
    # # print("---------2",acc1T)
    # acc1_1 = len(set(pre1_1).intersection(set(act1))) * len(set(pre1_1).intersection(set(act1)))/(len(pre1_1) * len(act1))
    # acc1_2 = len(set(pre1_2).intersection(set(act1))) * len(set(pre1_2).intersection(set(act1)))/(len(pre1_2) * len(act1))
    # acc1_3 = len(set(pre1_3).intersection(set(act1))) * len(set(pre1_3).intersection(set(act1)))/(len(pre1_3) * len(act1))
    # print("----",acc1)
    # print("Predicted Keywords : ",repA)
    # print("Actual Keywords : ",repB)
    # print("length of actual = ", len(repB))
    # print("length of predicted = ", len(repA))
    # print("similar word count = ", len(set(repA).intersection(set(repB))))
    # 26
    A2 = ['බිමට', 'ඔලිම්පික්']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['ක්රීඩා', 'උළෙලට', 'සහභාගී', 'වූ', 'නිලූක', 'කරුණාරත්න', 'චාමර', 'නුවන්', 'තරඟ', 'බිමට']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['නැති', 'කමද']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['ඔලිම්පික්', 'ක්රීඩා']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['ඔලිම්පික් ක්රීඩා උළෙලට සහභාගී වූ නිලූක කරුණාරත්න චාමර නුවන් තරඟ බිමට']
    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))

    acc2 = len(set(pre2).intersection(set(act2))) / (
                len(set(pre2).intersection(set(act2))) + (len(set(pre2).symmetric_difference(set(act2)))))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) / (
                len(set(pre2_1).intersection(set(act2))) + (len(set(pre2_1).symmetric_difference(set(act2)))))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) / (
                len(set(pre2_2).intersection(set(act2))) + (len(set(pre2_2).symmetric_difference(set(act2)))))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) / (
                len(set(pre2_3).intersection(set(act2))) + (len(set(pre2_3).symmetric_difference(set(act2)))))

    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # print("----------Done untill Here----------")
    # print("Accuracyyyyyy ",acc2)
    # 27
    A3 = ['පැවැත්වී', 'නියමිත', 'ක්රීඩා', 'උළෙලේ', 'භානුක', 'රාජපක්ෂ', 'තරඟ']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['ඔලිම්පික්', 'ක්රීඩා', 'අමාත්යවරයා']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['ලැබු', 'ප්රතිඵලය', 'තමන්', 'සතුටුට', 'පත්', 'නොවන', 'අතින්', 'උපාය', 'මාර්ගික', 'වරදක්', 'සිදුවු', 'මැතිව්', 'අබේසිංහ', 'පවසනව', 'ජය', 'පරාජය', 'ක්රීඩාවේ', 'අංගය', 'තම', 'ක්රීඩා', 'දිවිය', 'ජයග්රහණ', 'වගේම', 'පරාජයන්', 'අත්විද', 'පිහිණුම්', 'දක්ෂ', 'ප්රකාශ', 'කළා']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['මැතිව්', 'අබේසිංහ']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['ලැබු ප්රතිඵලය තමන් සතුටුට පත් නොවන තමන් අතින් උපාය මාර්ගික වරදක් සිදුවු මැතිව් අබේසිංහ පවසනව ජය පරාජය ක්රීඩාවේ අංගය තම ක්රීඩා දිවිය ජයග්රහණ වගේම පරාජයන් තමන් අත්විද පිහිණුම් දක්ෂ මැතිව් අබේසිංහ ප්රකාශ කළා']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))

    acc3 = len(set(pre1).intersection(set(act3))) / (
                len(set(pre1).intersection(set(act3))) + (len(set(pre1).symmetric_difference(set(act3)))))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) / (
                len(set(pre3_1).intersection(set(act3))) + (len(set(pre3_1).symmetric_difference(set(act3)))))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) / (
                len(set(pre3_2).intersection(set(act3))) + (len(set(pre3_2).symmetric_difference(set(act3)))))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) / (
                len(set(pre3_3).intersection(set(act3))) + (len(set(pre3_3).symmetric_difference(set(act3)))))

    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    # print("Accuracyyyyyy ", acc3)
    # 28
    A4 = ['ලෝකඩ', 'පදක්කම්']
    pre4 = list(dict.fromkeys(w for s in A4 for w in s.split()))
    A4_1 = ['දශක', 'ගණනාවක්', 'තිස්සේ', 'පිහිනුම්', 'ඉසව්', 'වලදී', 'පිරිමින්', 'පමණක', 'වැඩිදුර', 'තරග', 'නිර්දේශවූ', 'ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේදී', 'මීටර', 'දුර', 'නිදහස්', 'ආර', 'පිහිනීමට', 'කාන්තාවන්ට', 'ලබාදුන්', 'ප්රථම', 'අවස්ථාව', 'මෙවර', 'ටෝකියෝ', 'සිදුවිය', 'එහි', 'අවසන්', 'තරඟ', 'අද', 'පැවති', 'කේටි', 'ලෙඩෙක්', 'උළෙලේ', 'පදක්කම්']
    pre4_1 = list(dict.fromkeys(w for s in A4_1 for w in s.split()))
    A4_2 = ['ක්රීඩා', 'අමාත්යවරයා']
    pre4_2 = list(dict.fromkeys(w for s in A4_2 for w in s.split()))
    A4_3 = ['ටෝකියෝ', 'ඔලිම්පික්', 'උළෙලේදී', 'ශ්රී', 'ලංකාව', 'ලෙඩෙක්', 'දශක', 'පදක්කම්', 'සටහනේ', 'පළමු', 'ස්ථානයට', 'පැමිණීමට', 'සත්කාරක', 'ජපාන', 'සමත්', 'තිබේ', 'රන්', 'රිදී', 'ලෝකඩ', 'දිනාගෙන', 'ඇත']
    pre4_3 = list(dict.fromkeys(w for s in A4_3 for w in s.split()))
    B4 = ['දශක ගණනාවක් තිස්සේ පිහිනුම් ඉසව් වලදී පිරිමින් පමණක වැඩිදුර තරග නිර්දේශවූ ඔලිම්පික් ක්රීඩා උළෙලේදී මීටර දුර නිදහස් ආර පිහිනීමට කාන්තාවන්ට ලබාදුන් ප්රථම අවස්ථාව මෙවර ටෝකියෝ ඔලිම්පික් උළෙලේදී සිදුවිය එහි අවසන් තරඟ අද පැවති කේටි ලෙඩෙක්']
    act4 = list(dict.fromkeys(w for s in B4 for w in s.split()))


    acc4 = len(set(pre4).intersection(set(act4))) / (
                len(set(pre4).intersection(set(act4))) + (len(set(pre4).symmetric_difference(set(act4)))))
    acc4_1 = len(set(pre4_1).intersection(set(act4))) / (
                len(set(pre4_1).intersection(set(act4))) + (len(set(pre4_1).symmetric_difference(set(act4)))))
    acc4_2 = len(set(pre4_2).intersection(set(act4))) / (
                len(set(pre4_2).intersection(set(act4))) + (len(set(pre4_2).symmetric_difference(set(act4)))))
    acc4_3 = len(set(pre4_3).intersection(set(act4))) / (
                len(set(pre4_3).intersection(set(act4))) + (len(set(pre4_3).symmetric_difference(set(act4)))))


    acc4 = (acc4 + acc4_1 + acc4_2 + acc4_3) / 4

    # print("Accuracyyyyyy ", acc4)
    # 29
    A5 = ['මලල', 'ක්රීඩා', 'කණ්ඩාය']
    pre5 = list(dict.fromkeys(w for s in A5 for w in s.split()))
    A5_1 = ['ඔලිම්පික්', 'උළෙල', 'විස්තර', 'ඔස්ට්රේලියානු']
    pre5_1 = list(dict.fromkeys(w for s in A5_1 for w in s.split()))
    A5_2 = ['කණ්ඩාය', 'නිරෝධායනයට']
    pre5_2 = list(dict.fromkeys(w for s in A5_2 for w in s.split()))
    A5_3 = ['මළල', 'ක්රීඩා', 'ඉතිහාසයේ', 'පිටුවක', 'ලියන', 'බලාපොරොත්තු', 'ඇතුව', 'ජූලි', 'ඔලිම්පික්', 'අපි', 'සල්ලි', 'දීල', 'තියෙන්න', 'ක්රීඩකයන්', 'නිළ', 'ඇඳුම්', 'දෙන', 'එක', 'කමිටුවෙ', 'වැඩක්', 'අධ්යක්ෂ', 'ජනරාල්']
    pre5_3 = list(dict.fromkeys(w for s in A5_3 for w in s.split()))
    B5 = ['ඔස්ට්රේලියානු ඔලිම්පික් කණ්ඩාය නිරෝධායනයට මෙවර ඔලිම්පික් උළෙල සහභාගී ඔස්ට්රේලියානු මලල ක්රීඩා කණ්ඩාය නිරෝධායනයට යොමුකර තිබේ විස්තර']
    act5 = list(dict.fromkeys(w for s in B5 for w in s.split()))

    acc5 = len(set(pre5).intersection(set(act5))) / (
                len(set(pre5).intersection(set(act5))) + (len(set(pre5).symmetric_difference(set(act5)))))
    acc5_1 = len(set(pre5_1).intersection(set(act5))) / (
                len(set(pre5_1).intersection(set(act5))) + (len(set(pre5_1).symmetric_difference(set(act5)))))
    acc5_2 = len(set(pre5_2).intersection(set(act5))) / (
                len(set(pre5_2).intersection(set(act5))) + (len(set(pre5_2).symmetric_difference(set(act5)))))
    acc5_3 = len(set(pre5_3).intersection(set(act5))) / (
                len(set(pre5_3).intersection(set(act5))) + (len(set(pre5_3).symmetric_difference(set(act5)))))


    acc5 = (acc5 + acc5_1 + acc5_2 + acc5_3) / 4

    # print("Accuracyyyyyy ", acc5)
    # 30
    A6 = ['රාජපක්ෂ', 'මැතිතුමා', 'ත්']
    pre6 = list(dict.fromkeys(w for s in A6 for w in s.split()))
    A6_1 = ['කාටත', 'පුලුවන්']
    pre6_1 = list(dict.fromkeys(w for s in A6_1 for w in s.split()))
    A6_2 = ['ක්රීඩා', 'අමාත්යවරයා', 'ඉසව්', 'ජාතික', 'ලෝලීන්']
    pre6_2 = list(dict.fromkeys(w for s in A6_2 for w in s.split()))
    # A6_3 = ['භානුක', 'රාජපක්ෂ', 'හට', 'අවසන්', 'පන්දු', 'වාර', 'තරඟ', 'දෙකත්', 'අහිමි', 'ලකුණු', 'ලෝකෙ', 'රෙදි', 'මහන',
    #         'රටකට', 'ඔලිම්පික්', 'කණ්ඩායමට', 'ඒඒ', 'ක්රීඩාවට', 'අදාලව', 'ජාතික', 'ක්රීඩා', 'ඇදුම', 'සපයගන්න', 'බැරි',
    #         'වුවමනා', 'නැති', 'කමද', 'ගාණක්']
    # pre6_3 = list(dict.fromkeys(w for s in A6_3 for w in s.split()))
    B6 = ['කඟවේණුන්ගේ ජවය උරගා බැලෙන ඔලිම්පික් මලල ක්රීඩා වසන්තය ඇරඹේ']
    act6 = list(dict.fromkeys(w for s in B6 for w in s.split()))


    acc6 = len(set(pre6).intersection(set(act6))) / (
                len(set(pre6).intersection(set(act6))) + (len(set(pre6).symmetric_difference(set(act6)))))
    acc6_1 = len(set(pre6_1).intersection(set(act6))) / (
                len(set(pre6_1).intersection(set(act6))) + (len(set(pre6_1).symmetric_difference(set(act6)))))
    acc6_2 = len(set(pre6_2).intersection(set(act6))) / (
                len(set(pre6_2).intersection(set(act6))) + (len(set(pre6_2).symmetric_difference(set(act6)))))

    TP = 0
    FP = 0
    TH = 0.25

    if acc1 >= TH:
        TP = TP + 1
    elif acc1 < TH:
        FP = FP + 1

    if acc1_1 >= TH:
        TP = TP + 1
    elif acc1_1 < TH:
        FP = FP + 1

    if acc1_2 >= TH:
        TP = TP + 1
    elif acc1_2 < TH:
        FP = FP + 1

    if acc1_3 >= TH:
        TP = TP + 1
    elif acc1_3 < TH:
        FP = FP + 1

    if acc2 >= TH:
        TP = TP + 1
    elif acc2 < TH:
        FP = FP + 1

    if acc2_1 >= TH:
        TP = TP + 1
    elif acc2_1 < TH:
        FP = FP + 1

    if acc2_2 >= TH:
        TP = TP + 1
    elif acc2_2 < TH:
        FP = FP + 1

    if acc2_3 >= TH:
        TP = TP + 1
    elif acc2_3 < TH:
        FP = FP + 1

    if acc3 >= TH:
        TP = TP + 1
    elif acc3_1 < TH:
        FP = FP + 1

    if acc3_2 >= TH:
        TP = TP + 1
    elif acc3_2 < TH:
        FP = FP + 1

    if acc3_3 >= TH:
        TP = TP + 1
    elif acc3_3 < TH:
        FP = FP + 1

    if acc4 >= TH:
        TP = TP + 1
    elif acc4 < TH:
        FP = FP + 1

    if acc4_1 >= TH:
        TP = TP + 1
    elif acc4_1 < TH:
        FP = FP + 1

    if acc4_2 >= TH:
        TP = TP + 1
    elif acc4_2 < TH:
        FP = FP + 1

    if acc4_3 >= TH:
        TP = TP + 1
    elif acc4_3 < TH:
        FP = FP + 1

    if acc5 >= TH:
        TP = TP + 1
    elif acc5 < TH:
        FP = FP + 1

    if acc5_1 >= TH:
        TP = TP + 1
    elif acc5_1 < TH:
        FP = FP + 1

    if acc5_2 >= TH:
        TP = TP + 1
    elif acc5_2 < TH:
        FP = FP + 1

    if acc5_3 >= TH:
        TP = TP + 1
    elif acc5_3 < TH:
        FP = FP + 1

    if acc6 >= TH:
        TP = TP + 1
    elif acc6 < TH:
        FP = FP + 1

    if acc6_1 >= TH:
        TP = TP + 1
    elif acc6_1 < TH:
        FP = FP + 1

    if acc6_2 >= TH:
        TP = TP + 1
    elif acc6_2 < TH:
        FP = FP + 1


    BPrecision = (TP / (TP + FP))


    print("Overall Precision for Bigram ::::::", BPrecision)


# coding=utf-8

def accuracy_trigram_keyword_accuracy():

    print("---------------------------Keyword Accuracy Calculating(trigram)-------------------------")

    TP = 0
    FP = 0
    print("")
    # 25
    A1 = ['ක්රීඩා', 'කරන', 'කෙනෙක්', 'අමාත්යවරයා', 'උනා', 'කිව්වතරුණයෙක්', 'කිව්ව', 'ලැජ්ජ', 'වෙන්න', 'ඕනෙ']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['වෙන්න', 'ඕනෙ', 'ක්රීඩා', 'කරන']
    pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
    A1_2 = ['ක්රීඩා', 'උළෙලේ', 'ප්රථම', 'රන්', 'පදක්කම', 'චීනය', 'සෞඛ්යය', 'වල', 'විවිධත්ව', 'සමානාත්මතාව', 'ප්රවර්ධන', 'කිරීම', 'ලෝක', 'සංවිධානය', 'අවබෝධතා', 'ගිවිසුමක්', 'අත්සන', 'කරයි', 'භානුක', 'රාජපක්ෂ', 'අද', 'තරඟ', 'අවිනිශ්චිත', 'තත්වය', 'වාර්තා', 'වනවා', 'තවම', 'නිශ්චිතව', 'සම්බන්ධව', 'කිසිදු', 'ලෙසකින්', 'දන්වා', 'නැත', 'ඔලිම්පික්', 'මිල්කා', 'ගිහානී', 'තැනට', 'දේශපාලනය', 'පෙරලුණාට', 'ක්රීඩාව', 'පෙරලන්න', 'බැහැ', 'ඕස්ට්රේලියා', 'මලල', 'කණ්', 'නිවස්', 'වලට', 'පැය', 'බාගෙම', 'කිව්වෙ', 'මරණෙ', 'පුවත්වලට', 'ගියෙට්', 'ක්රිකට්', 'ටීම්', 'එකේ', 'සයිලන්ස්', 'කරන', 'වෙන්න', 'ඕනෙ', 'උළෙල', 'නියෝජන', 'රිද්මයානූකූල', 'ජිම්නාස්ටික්', 'ඉසව්', 'ඉදිරිපත්', 'වූ', 'ශ්රීලාංකික', 'කන්ඩායම', 'නායිකා', 'සිල්වා', 'සහභාගි', 'මූලික', 'වටයේදී', 'පලමු', 'තරඟයේ', 'ස්ථානය', 'ලබා', 'ගනිමින්', 'අවසන්', 'කර', 'තිබේ', 'ඇයට', 'වට', 'ඉතිරිව', 'තිබෙනව', 'සිය', 'දක්ෂතා', 'පෙන්වීම', 'අඩුව', 'අපි', 'දැණුනා', 'පන්දු', 'යැවීම', 'හදාගන්න', 'සෑහෙන', 'කැපකිරීම්', 'කළා', 'පැතුම්', 'ටත්', 'ආබාධ', 'තරඟයෙන්', 'අනතුරුව', 'පැවති', 'මාධ්ය', 'හමුව']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේ']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['ක්රීඩා කරන කෙනෙක් අමාත්යවරයා උනා කිව්වතරුණයෙක් ක්රීඩා අමාත්යවරයා උනා කිව්ව ලැජ්ජ වෙන්න ඕනෙ']
    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))

    acc1 = len(set(pre1).intersection(set(act1))) / (
                len(set(pre1).intersection(set(act1))) + (len(set(pre1).symmetric_difference(set(act1)))))
    acc1_1 = len(set(pre1_1).intersection(set(act1))) / (
                len(set(pre1_1).intersection(set(act1))) + (len(set(pre1_1).symmetric_difference(set(act1)))))
    acc1_2 = len(set(pre1_2).intersection(set(act1))) / (
                len(set(pre1_2).intersection(set(act1))) + (len(set(pre1_2).symmetric_difference(set(act1)))))
    acc1_3 = len(set(pre1_3).intersection(set(act1))) / (
                len(set(pre1_3).intersection(set(act1))) + (len(set(pre1_3).symmetric_difference(set(act1)))))



    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3) / 4

    A2 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලට', 'සහභාගී', 'වූ', 'නිලූක', 'කරුණාරත්න', 'චාමර', 'නුවන්', 'තරඟ', 'බිමට']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['ඔලිම්පික්', 'අද', 'තරග', 'ඉසව්', 'ටෝකියෝ', 'ක්රීඩා', 'උළලේ', 'තුන්වන', 'දිනය', 'අදයි', 'විස්තර', 'භානුක', 'රාජපක්ෂ', 'අහිමි', 'ලකුණු', 'නිලූකගෙ', 'පරණ', 'එකක්', 'දිග', 'වෙන්නෙ', 'කියලා', 'බැලුවා', 'බලද්දි', 'චාමිකගෙ', 'ලා', 'ඇවිත', 'දාන්', 'අරං', 'වලින්', 'මොන', 'තිබුණත්', 'වැඩක්', 'ක්රිකට්ම', 'ගහන්න', 'ඕන', 'ජනප්රිය', 'වෙන්න', 'නං', 'දෙවනි', 'එකට', 'නෑලු', 'උළෙලක', 'සුදුසුකම්', 'ලැබූ', 'පළමු', 'ශ්රී', 'ලාංකේය', 'ජිම්නාස්ටික්', 'ක්රීඩිකාව', 'මිල්කා', 'ගෙහානි', 'ඇයගේ', 'දක්ෂතා', 'විනය', 'ක්රීඩාව', 'කෙරෙහි', 'දක්වන', 'කැපවී', 'ආදී', 'වූ', 'සාධක', 'මතින්', 'තරඟබිමේදි', 'මව්රටට', 'ගෞරවයක්', 'ගෙනදෙමින්', 'කළා', 'වයස', 'අවුරුදු', 'ක්වූ', 'ජපානයේ', 'මොමිජි', 'නිෂියා', 'සඳුදා', 'නුවර', 'පැවති', 'උළෙලේ', 'කාන්තා', 'වීදි', 'ස්කේට්බොඩිං', 'ක්රීඩාවේ', 'ප්රථම', 'රන්', 'පදක්කම', 'දිනා', 'ගනිමින්', 'ඉතිහාසය', 'අලුත', 'කළාය', 'රිදී', 'දිනාගත්', 'බ්රසීලයේ', 'රයිසා', 'ලීල්ද', 'දැරියකවූ', 'හැවිරිදි', 'ජප', 'ලෝකෙ', 'රෙදි', 'නැති', 'කමද', 'ගරු', 'තරුණ', 'අමාත්ය', 'නාමල්', 'මැතිතුමන්', 'එක්සත', 'ජාතීන්', 'මානුෂීය', 'කටයුතු', 'ප', 'ජාතික', 'වොලිබෝල්', 'හෝ', 'අනෙකු', 'තරඟ', 'පාපන්දු', 'බාස්කට්', 'බෝල්', 'රගර්', 'පැරද්දෙදි', 'මිනිස්සු', 'කෑගහන්නෙ', 'නැත්තෙ', 'ලංකාව', 'ඉන්නෙ', 'ලෝලීන්', 'ක්රිකට්', 'ලෝලින්ද', 'වර්ල්ඩ්', 'කප්', 'දින්නන්නම', 'වෙයි', 'අනිත්', 'ඒව', 'කා', 'වදින්න', 'ගනන්', 'වල', 'ලෝලියා']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['තරඟ', 'බිමට', 'ඔලිම්පික්', 'ක්රීඩා']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['භානුක', 'රාජපක්ෂ', 'හට', 'අවසන්', 'පන්දු', 'වාර', 'තරඟ', 'දෙකත්', 'අහිමි', 'ලකුණු', 'ලෝකෙ', 'රෙදි', 'මහන', 'රටකට', 'ඔලිම්පික්', 'කණ්ඩායමට', 'ඒඒ', 'ක්රීඩාවට', 'අදාලව', 'ජාතික', 'ක්රීඩා', 'ඇදුම', 'සපයගන්න', 'බැරි', 'වුවමනා', 'නැති', 'කමද', 'ගාණක්']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['ඔලිම්පික් ක්රීඩා උළෙලට සහභාගී වූ නිලූක කරුණාරත්න චාමර නුවන් තරඟ බිමට']
    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))

    acc2 = len(set(pre2).intersection(set(act2))) / (
            len(set(pre2).intersection(set(act2))) + (len(set(pre2).symmetric_difference(set(act2)))))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) / (
            len(set(pre2_1).intersection(set(act2))) + (len(set(pre2_1).symmetric_difference(set(act2)))))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) / (
            len(set(pre2_2).intersection(set(act2))) + (len(set(pre2_2).symmetric_difference(set(act2)))))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) / (
            len(set(pre2_3).intersection(set(act2))) + (len(set(pre2_3).symmetric_difference(set(act2)))))


    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # print("----------Done untill Here----------")
    # print("Accuracyyyyyy ",acc2)
    # 27
    A3 = ['මම', 'හිතන්නේ', 'මුළු', 'ජීවිත', 'කාලෙම', 'රජයෙන්', 'එයාට', 'පහසුකම්', 'සපයන්න', 'ඕනි', 'කියලාඑයා', 'ලබපු', 'ජයග්ර']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['ලැබු', 'ප්රතිඵලය', 'තමන්', 'සතුටුට', 'පත්', 'නොවන', 'අතින්', 'උපාය', 'මාර්ගික', 'වරදක්', 'සිදුවු', 'මැතිව්', 'අබේසිංහ', 'පවසනව', 'ජය', 'පරාජය', 'ක්රීඩාවේ', 'අංගය', 'තම', 'ක්රීඩා', 'දිවිය', 'ජයග්රහණ', 'වගේම', 'පරාජයන්', 'අත්විද', 'පිහිණුම්', 'දක්ෂ', 'ප්රකාශ', 'කළා']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['ප්රකාශ', 'කළා', 'ලැබු', 'ප්රතිඵලය']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේ']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['ලැබු ප්රතිඵලය තමන් සතුටුට පත් නොවන තමන් අතින් උපාය මාර්ගික වරදක් සිදුවු මැතිව් අබේසිංහ පවසනව ජය පරාජය ක්රීඩාවේ අංගය තම ක්රීඩා දිවිය ජයග්රහණ වගේම පරාජයන් තමන් අත්විද පිහිණුම් දක්ෂ මැතිව් අබේසිංහ ප්රකාශ කළා']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))

    acc3 = len(set(pre1).intersection(set(act3))) / (
            len(set(pre1).intersection(set(act3))) + (len(set(pre1).symmetric_difference(set(act3)))))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) / (
            len(set(pre3_1).intersection(set(act3))) + (len(set(pre3_1).symmetric_difference(set(act3)))))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) / (
            len(set(pre3_2).intersection(set(act3))) + (len(set(pre3_2).symmetric_difference(set(act3)))))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) / (
            len(set(pre3_3).intersection(set(act3))) + (len(set(pre3_3).symmetric_difference(set(act3)))))


    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    # print("Accuracyyyyyy ", acc3)
    # 28
    A4 = ['කේටි', 'ලෙඩෙක්', 'දශක', 'ගණනාවක්', 'උළෙලේ', 'පදක්කම්', 'සටහනේ', 'පළමු', 'ස්ථානයට', 'පැමිණීමට', 'රන්', 'රිදී', 'ලෝකඩ', 'දිනාගෙන', 'ඇත']
    pre4 = list(dict.fromkeys(w for s in A4 for w in s.split()))
    A4_1 = ['දශක', 'ගණනාවක්', 'තිස්සේ', 'පිහිනුම්', 'ඉසව්', 'වලදී', 'පිරිමින්', 'පමණක', 'වැඩිදුර', 'තරග', 'නිර්දේශවූ', 'ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේදී', 'මීටර', 'දුර', 'නිදහස්', 'ආර', 'පිහිනීමට', 'කාන්තාවන්ට', 'ලබාදුන්', 'ප්රථම', 'අවස්ථාව', 'මෙවර', 'ටෝකියෝ', 'සිදුවිය', 'එහි', 'අවසන්', 'තරඟ', 'අද', 'පැවති', 'කේටි', 'ලෙඩෙක්', 'උළෙලේ', 'පදක්කම්']
    pre4_1 = list(dict.fromkeys(w for s in A4_1 for w in s.split()))
    A4_2 = ['ඔලිම්පික්', 'ක්රීඩා', 'උළෙලේ', 'ස්ථානයට', 'පැමිණීමට', 'චීනය', 'සමත්', 'තිබේ', 'රන්', 'පදක්කම්', 'දිනාගෙන', 'ඇත', 'දෙවන', 'ස්ථානයේ', 'රැදී', 'සිටින', 'සත්කාරක', 'ජපාන', 'රිදී', 'ලෝකඩ', 'ජයග්රහණ', 'කර', 'අද', 'හඳුනාගත', 'ආසාදිතයින්', 'ගම්මානයට', 'අදාළ', 'නැහැ', 'සංවිධායකයින්', 'පවසයි']
    pre4_2 = list(dict.fromkeys(w for s in A4_2 for w in s.split()))
    A4_3 = ['කුර්නාල්', 'පාණ්ඩ්යො', 'ආශ්රීතයන්', 'ශිකර්', 'ධවාන්', 'හාර්දික්', 'පෘථිවි', 'ෂෝ', 'සුර්යකුමාර්', 'යාදෙව්', 'ඉෂාන්', 'කිෂන්', 'මනිෂ්', 'පාණ්ඩේ', 'කේ', 'ගෞතම', 'යුෂ්වේන්ද්ර', 'චාහල්', 'ක්රීඩකයි', 'දෙනා', 'ඉදිරි', 'තරග', 'දෙක', 'ක්රීඩා', 'කිරීමට', 'හැකියා', 'කර', 'තිබේ', 'ඔලිම්පික්', 'ශ්රී', 'ලංකාව', 'ඉන්දියාව', 'සංවිධායකයින්', 'පවසයි', 'අද', 'හඳුනාගත']
    pre4_3 = list(dict.fromkeys(w for s in A4_3 for w in s.split()))
    B4 = ['දශක ගණනාවක් තිස්සේ පිහිනුම් ඉසව් වලදී පිරිමින් පමණක වැඩිදුර තරග නිර්දේශවූ ඔලිම්පික් ක්රීඩා උළෙලේදී මීටර දුර නිදහස් ආර පිහිනීමට කාන්තාවන්ට ලබාදුන් ප්රථම අවස්ථාව මෙවර ටෝකියෝ ඔලිම්පික් උළෙලේදී සිදුවිය එහි අවසන් තරඟ අද පැවති කේටි ලෙඩෙක්']
    act4 = list(dict.fromkeys(w for s in B4 for w in s.split()))

    acc4 = len(set(pre4).intersection(set(act4))) / (
            len(set(pre4).intersection(set(act4))) + (len(set(pre4).symmetric_difference(set(act4)))))
    acc4_1 = len(set(pre4_1).intersection(set(act4))) / (
            len(set(pre4_1).intersection(set(act4))) + (len(set(pre4_1).symmetric_difference(set(act4)))))
    acc4_2 = len(set(pre4_2).intersection(set(act4))) / (
            len(set(pre4_2).intersection(set(act4))) + (len(set(pre4_2).symmetric_difference(set(act4)))))
    acc4_3 = len(set(pre4_3).intersection(set(act4))) / (
            len(set(pre4_3).intersection(set(act4))) + (len(set(pre4_3).symmetric_difference(set(act4)))))


    acc4 = (acc4 + acc4_1 + acc4_2 + acc4_3) / 4

    # print("Accuracyyyyyy ", acc4)
    # 29
    A5 = ['තිබේ', 'විස්තර', 'ඔස්ට්රේලියානු', 'ඔලිම්පික්']
    pre5 = list(dict.fromkeys(w for s in A5 for w in s.split()))
    A5_1 = ['මෙවර', 'ඔලිම්පික්', 'උළෙල', 'සහභාගී', 'ඔස්ට්රේලියානු', 'මලල', 'ක්රීඩා', 'කණ්ඩාය', 'නිරෝධායනයට', 'යොමුකර', 'තිබේ']
    pre5_1 = list(dict.fromkeys(w for s in A5_1 for w in s.split()))
    A5_2 = ['මලල', 'ක්රීඩා', 'කණ්ඩාය', 'නිරෝධායනයට']
    pre5_2 = list(dict.fromkeys(w for s in A5_2 for w in s.split()))
    A5_3 = ['ඔස්ට්රේලියානු', 'ඔලිම්පික්', 'කණ්ඩාය', 'නිරෝධායනයට', 'මෙවර', 'යොමුකර', 'තිබේ', 'විස්තර']
    pre5_3 = list(dict.fromkeys(w for s in A5_3 for w in s.split()))
    B5 = ['ඔස්ට්රේලියානු ඔලිම්පික් කණ්ඩාය නිරෝධායනයට මෙවර ඔලිම්පික් උළෙල සහභාගී ඔස්ට්රේලියානු මලල ක්රීඩා කණ්ඩාය නිරෝධායනයට යොමුකර තිබේ විස්තර']
    act5 = list(dict.fromkeys(w for s in B5 for w in s.split()))

    acc5 = len(set(pre5).intersection(set(act5))) / (
            len(set(pre5).intersection(set(act5))) + (len(set(pre5).symmetric_difference(set(act5)))))
    acc5_1 = len(set(pre5_1).intersection(set(act5))) / (
            len(set(pre5_1).intersection(set(act5))) + (len(set(pre5_1).symmetric_difference(set(act5)))))
    acc5_2 = len(set(pre5_2).intersection(set(act5))) / (
            len(set(pre5_2).intersection(set(act5))) + (len(set(pre5_2).symmetric_difference(set(act5)))))
    acc5_3 = len(set(pre5_3).intersection(set(act5))) / (
            len(set(pre5_3).intersection(set(act5))) + (len(set(pre5_3).symmetric_difference(set(act5)))))


    acc5 = (acc5 + acc5_1 + acc5_2 + acc5_3) / 4

    # print("Accuracyyyyyy ", acc5)
    # 30
    A6 = ['රාජපක්ෂ', 'මැතිතුමා', 'ත්']
    pre6 = list(dict.fromkeys(w for s in A6 for w in s.split()))
    A6_1 = ['ස්ථානය', 'ලබා', 'ගනිමින්', 'තරඟ', 'අවසන්', 'වසන්තය', 'ඇරඹේ', 'කඟවේණුන්ගේ', 'ජවය', 'කියලා', 'වැඩක්', 'නැහැ', 'ටීම්', 'එකක', 'කැපවී', 'අවතක්සේරු', 'කරනවා', 'කවදාවත්', 'ක්රීඩා', 'කරලා', 'නැතුව', 'ඔලිම්පික්', 'තරග', 'වූ', 'තැන', 'කොහොම', 'අපේ', 'ඇමතිතුමා', 'ලස්සන', 'චීනයේ', 'මුලු', 'ක්ෂේත්රයට', 'විරුද්ධව', 'දැඩි', 'බොරු', 'ප්රචාරය', 'බටහිර', 'අධිරාජ්යවාදී', 'මාද්ය', 'ගෙන', 'යන්නේ', 'නිසවෙනි', 'ජයග්රහන', 'සමාජවාදී', 'ඒකාදිපතියන්ගේ', 'කුමණ්ත්රනයක්', 'හුවා', 'දක්වමින්', 'සිටී', 'ඉන්දියාව', 'පැවති', 'මැතිතුමා', 'ත්', 'ටෝකියෝ', 'ඔලිම්පික්හි', 'වෙනි', 'දින', 'අද', 'මලල', 'ඉසව්', 'ආරම්භ', 'කරමින්', 'ඉසව්වෙ', 'සිව්වන', 'මූලික', 'වටයට', 'ඉරිපත්', 'ශ්රීලංකා', 'ක්රීඩික', 'නිමාලි', 'ලියනආරච්චි', 'එහි', 'කරන', 'ලදී', 'සංගම්', 'නියාමන', 'පාර්ලිමේන්තු', 'පනත', 'ජාතික', 'තේමා', 'ගීතය', 'ජය', 'හඹා', 'ලොවම', 'කළඹන', 'බය', 'නොබා', 'පෙරට', 'පරදමින්', 'පරාජිත', 'අභියෝග', 'කරයි', 'ලොවට', 'පැරදුම', 'පරදන', 'කාටත', 'පුලුවන්', 'දිරියෙන්', 'දිදුළන', 'ජව', 'පිටිය', 'ජයගෙන', 'දිය', 'දෙබෑ', 'කරන්', 'පිහිනන', 'හිරු', 'පරාද', 'කර', 'අවදිව', 'නිමා', 'කළේ', 'අදිටන', 'අරමුණ', 'හඳුනන', 'ඔබලා', 'ඉතාලි', 'ක්රිකට්', 'කණ්ඩායමේ', 'කුඩාම', 'කණ්ඩායමක්', 'පුහුණු', 'කළ', 'යුතුයිඑක්කෝ', 'ඔබේ', 'සිව්', 'වරක්', 'කිරුළු', 'දැරූ', 'ජිම්නාස්ටික්', 'ශූරි', 'ලෝලීන්', 'ඇස්', 'කඳුළ', 'එක්', 'විනය', 'කමිටුවෙන්', 'නිර්දේශිත', 'දඬුවම්', 'විධායක', 'කමිටු', 'යළි', 'සලකා', 'බැලීමේ', 'අගය', 'යුතුයි', 'ලැබුණු', 'අවස්ථාවෙන්', 'ප්රයෝජන', 'අරගෙන', 'හොඳ', 'වෙලා', 'තහනම්', 'කාලයෙන්', 'පසුව', 'රට', 'කැපවීමෙන්', 'කරන්න']
    pre6_1 = list(dict.fromkeys(w for s in A6_1 for w in s.split()))
    A6_2 = ['කඟවේණුන්ගේ', 'ජවය', 'උරගා', 'බැලෙන', 'ඔලිම්පික්', 'මලල', 'ක්රීඩා', 'වසන්තය', 'ඇරඹේ', 'තරග', 'අද', 'පැවැත්වුණ', 'මීටර', 'කාන්තා', 'ඉසව්වේදී', 'නිමාලි', 'හිමි', 'වූ', 'තැන', 'කොහොම', 'අපේ', 'ඇමතිතුමා', 'ලස්සන', 'ඉන්දියාව', 'පැවති', 'තරගාවලිය', 'ජයග්රහණ', 'කරා', 'මෙහෙයවූ', 'අතිගරු', 'ගෝඨාබය', 'රාජපක්ෂ', 'ජනාධිපති', 'තුමා', 'ත්', 'අගමැති', 'මහින්ද', 'මැතිතුමා', 'අමාත්යවරයා', 'නාමල්', 'තිරය', 'පිටුපස', 'සිටිමින්', 'සැබෑ', 'නායකත්ව', 'දුන්', 'බැසිල්']
    pre6_2 = list(dict.fromkeys(w for s in A6_2 for w in s.split()))
    # A6_3 = ['භානුක', 'රාජපක්ෂ', 'හට', 'අවසන්', 'පන්දු', 'වාර', 'තරඟ', 'දෙකත්', 'අහිමි', 'ලකුණු', 'ලෝකෙ', 'රෙදි', 'මහන',
    #         'රටකට', 'ඔලිම්පික්', 'කණ්ඩායමට', 'ඒඒ', 'ක්රීඩාවට', 'අදාලව', 'ජාතික', 'ක්රීඩා', 'ඇදුම', 'සපයගන්න', 'බැරි',
    #         'වුවමනා', 'නැති', 'කමද', 'ගාණක්']
    # pre6_3 = list(dict.fromkeys(w for s in A6_3 for w in s.split()))
    B6 = ['කඟවේණුන්ගේ ජවය උරගා බැලෙන ඔලිම්පික් මලල ක්රීඩා වසන්තය ඇරඹේ']
    act6 = list(dict.fromkeys(w for s in B6 for w in s.split()))


    acc6 = len(set(pre6).intersection(set(act6))) / (
                len(set(pre6).intersection(set(act6))) + (len(set(pre6).symmetric_difference(set(act6)))))
    acc6_1 = len(set(pre6_1).intersection(set(act6))) / (
                len(set(pre6_1).intersection(set(act6))) + (len(set(pre6_1).symmetric_difference(set(act6)))))
    acc6_2 = len(set(pre6_2).intersection(set(act6))) / (
                len(set(pre6_2).intersection(set(act6))) + (len(set(pre6_2).symmetric_difference(set(act6)))))

    TP = 0
    FP = 0
    TH = 0.25

    if acc1 >= TH:
        TP = TP + 1
    elif acc1 < TH:
        FP = FP + 1

    if acc1_1 >= TH:
        TP = TP + 1
    elif acc1_1 < TH:
        FP = FP + 1

    if acc1_2 >= TH:
        TP = TP + 1
    elif acc1_2 < TH:
        FP = FP + 1

    if acc1_3 >= TH:
        TP = TP + 1
    elif acc1_3 < TH:
        FP = FP + 1

    if acc2 >= TH:
        TP = TP + 1
    elif acc2 < TH:
        FP = FP + 1

    if acc2_1 >= TH:
        TP = TP + 1
    elif acc2_1 < TH:
        FP = FP + 1

    if acc2_2 >= TH:
        TP = TP + 1
    elif acc2_2 < TH:
        FP = FP + 1

    if acc2_3 >= TH:
        TP = TP + 1
    elif acc2_3 < TH:
        FP = FP + 1

    if acc3 >= TH:
        TP = TP + 1
    elif acc3_1 < TH:
        FP = FP + 1

    if acc3_2 >= TH:
        TP = TP + 1
    elif acc3_2 < TH:
        FP = FP + 1

    if acc3_3 >= TH:
        TP = TP + 1
    elif acc3_3 < TH:
        FP = FP + 1

    if acc4 >= TH:
        TP = TP + 1
    elif acc4 < TH:
        FP =  FP +1

    if acc4_1 >= TH:
        TP = TP + 1
    elif acc4_1 < TH:
        FP =  FP +1

    if acc4_2 >= TH:
        TP = TP + 1
    elif acc4_2 < TH:
        FP =  FP +1

    if acc4_3 >= TH:
        TP = TP + 1
    elif acc4_3 < TH:
        FP =  FP +1

    if acc5 >= TH:
        TP = TP + 1
    elif acc5 < TH:
        FP =  FP +1

    if acc5_1 >= TH:
        TP = TP + 1
    elif acc5_1 < TH:
        FP =  FP +1

    if acc5_2 >= TH:
        TP = TP + 1
    elif acc5_2 < TH:
        FP =  FP +1

    if acc5_3 >= TH:
        TP = TP + 1
    elif acc5_3 < TH:
        FP =  FP +1

    if acc6 >= TH:
        TP = TP + 1
    elif acc6 < TH:
        FP =  FP +1

    if acc6_1 >= TH:
        TP = TP + 1
    elif acc6_1 < TH:
        FP =  FP +1

    if acc6_2 >= TH:
        TP = TP + 1
    elif acc6_2 < TH:
        FP =  FP +1


    TPrecision = (TP/(TP +FP))

    print("Overall Precision for Trigram ::::::", TPrecision)






# driver code
if __name__ == '__main__':
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Short Term Trends - Precision  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    accuracy_unigram_keyword_accuracy()
    print(" ")
    accuracy_bigram_keyword_accuracy()
    print(" ")
    accuracy_trigram_keyword_accuracy()
    print(" ")


    # unique()