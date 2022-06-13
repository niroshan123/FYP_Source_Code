# coding=utf-8

# accuracy = TP / TP + FP
# Intersects with actual / Intersect with actual + (length of predicted - Intersect with actual)

def accuracy_unigram_keyword_accuracy():

    print("---------------------------Keyword Accuracy Calculating(Unigram)-------------------------")
    print("")
    # Considering sports
    A1 = ['හිතාමතා', 'දුර්වල', 'විලාසයක', 'නිරත']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['ලංකාව', 'ක්රීඩා', 'ශ්රී', 'සිය', 'දිවියේ', 'ද', 'වසරේ', 'ලෝක', 'ඔහුගේ', 'කී', 'එකක්', 'වැඩි', 'විස්තර']
    pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
    A1_2 = ['අද', 'කිරීමට', 'එරෙහි', 'නරඹන්න', 'ක්රිකට්', 'කුසලා', 'තරගාවලියට', 'තරගාවලිය']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['තරගාවලිය', 'හිතාමතා', 'දුර්වල', 'විලාසයක', 'නිරත']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['නායක', 'දසුන්', 'ශානක', 'ලංකාව', 'ක්රිකට්', 'දකුණු අප්රිකාව','දුර්වල', 'ක්රීඩා', 'විලාසයක', 'විස්සයි විස්ස', 'ක්රිකට්', 'තරගාවලිය','පරාජයෙන්','විස්තර']

    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))
    acc1 = len(set(pre1).intersection(set(act1))) * len(set(pre1).intersection(set(act1)))/(len(pre1) * len(act1))
    acc1_1 = len(set(pre1_1).intersection(set(act1))) * len(set(pre1_1).intersection(set(act1)))/(len(pre1_1) * len(act1))
    acc1_2 = len(set(pre1_2).intersection(set(act1))) * len(set(pre1_2).intersection(set(act1)))/(len(pre1_2) * len(act1))
    acc1_3 = len(set(pre1_3).intersection(set(act1))) * len(set(pre1_3).intersection(set(act1)))/(len(pre1_3) * len(act1))
    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3)/4
    # Considering Politics
    A2 = ['පාර්ලිමේන්තු', 'කබ්රාල්', 'දී', 'ජොන්ස්ටන්ගෙන්', 'මහ', 'තනතුර', 'බාරගැනීම', 'අස්වී', 'සැරසෙයි']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['රාජ්ය', 'මන්ත්රී', 'කියයි', 'මේ', 'සාමාන්', 'කරන්න']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['පොරොන්දු', 'මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['සහ', 'ක්රීඩා', 'නෑ', 'අමාත්යවරයා', 'සංවර්ධන', 'කණ්ඩායමක්', 'වසංගත']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම', 'අමාත්යවරයා','මහ', 'බැංකු', 'අධිපති', 'තනතුර', 'බාරගැනීම', 'කබ්රාල්','සැරසෙයි']

    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))
    acc2 = len(set(act2).intersection(set(pre2))) * len(set(act2).intersection(set(pre2))) / (len(act2) * len(pre2))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) * len(set(pre2_1).intersection(set(act2))) / (
                len(pre2_1) * len(act2))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) * len(set(pre2_2).intersection(set(act2))) / (
            len(pre2_2) * len(act2))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) * len(set(pre2_3).intersection(set(act2))) / (
            len(pre2_3) * len(act2))
    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # print("Accuracyyyyyy ",acc2)
    # Considering Crime
    A3 = ['අනුරාධපුර', 'බන්ධනාගාරයේ', 'මකන්න', 'උත්සාහයක', 'සිරකරු', 'දෙදෙනෙකු', 'දණගස්වා', 'ඔවුන්ගේ', 'හිසට', 'පිස්තෝල', 'තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ', 'රාජ්ය', 'අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත', 'වහා', 'අත්අඩංගුව', 'ගනු']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['අත්අඩංගුව', 'ගත්', 'බව']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['අමාත්යවරයා', 'බලා', 'නිලධාරින්', 'ලොක්ක']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['සිරකරු', 'දෙදෙනෙකු','බන්ධනාගාරයේ','තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ','බන්ධනාගාර','අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත','අත්අඩංගුව']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))
    acc3 = len(set(act3).intersection(set(pre3))) * len(set(act3).intersection(set(pre3))) / (len(act3) * len(pre3))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) * len(set(pre3_1).intersection(set(act3))) / (
            len(pre3_1) * len(act3))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) * len(set(pre3_2).intersection(set(act3))) / (
            len(pre3_2) * len(act3))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) * len(set(pre3_3).intersection(set(act3))) / (
            len(pre3_3) * len(act3))
    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    TP = 0
    FP = 0
    TH = 0.3

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

    UPrecision = (TP / (TP + FP))

    print("Overall Precision for Unigram ::::::", UPrecision)

    # print("Accuracyyyyyy ", acc3)
    # Considering Politics
    # A4 = []
    # pre4 = list(dict.fromkeys(w for s in A4 for w in s.split()))
    # A4_1 = []
    # pre4_1 = list(dict.fromkeys(w for s in A4_1 for w in s.split()))
    # A4_2 = []
    # pre4_2 = list(dict.fromkeys(w for s in A4_2 for w in s.split()))
    # A4_3 = []
    # pre4_3 = list(dict.fromkeys(w for s in A4_3 for w in s.split()))
    # B4 = []
    # act4 = list(dict.fromkeys(w for s in B4 for w in s.split()))
    # acc4 = len(set(act4).intersection(set(pre4))) * len(set(act4).intersection(set(pre4))) / (len(act4) * len(pre4))
    # acc4_1 = len(set(pre4_1).intersection(set(act4))) * len(set(pre4_1).intersection(set(act4))) / (
    #         len(pre4_1) * len(act4))
    # acc4_2 = len(set(pre4_2).intersection(set(act4))) * len(set(pre4_2).intersection(set(act4))) / (
    #         len(pre4_2) * len(act4))
    # acc4_3 = len(set(pre4_3).intersection(set(act4))) * len(set(pre4_3).intersection(set(act4))) / (
    #         len(pre4_3) * len(act4))
    # acc4 = (acc4 + acc4_1 + acc4_2 + acc4_3) / 4
    #
    # # print("Accuracyyyyyy ", acc4)
    # # 29
    # A5 = []
    # pre5 = list(dict.fromkeys(w for s in A5 for w in s.split()))
    # A5_1 = []
    # pre5_1 = list(dict.fromkeys(w for s in A5_1 for w in s.split()))
    # A5_2 = []
    # pre5_2 = list(dict.fromkeys(w for s in A5_2 for w in s.split()))
    # A5_3 = []
    # pre5_3 = list(dict.fromkeys(w for s in A5_3 for w in s.split()))
    # B5 = []
    # act5 = list(dict.fromkeys(w for s in B5 for w in s.split()))
    # acc5 = len(set(act5).intersection(set(pre5))) * len(set(act5).intersection(set(pre5))) / (len(act5) * len(pre5))
    # acc5_1 = len(set(pre5_1).intersection(set(act5))) * len(set(pre5_1).intersection(set(act5))) / (
    #         len(pre5_1) * len(act5))
    # acc5_2 = len(set(pre5_2).intersection(set(act5))) * len(set(pre5_2).intersection(set(act5))) / (
    #         len(pre5_2) * len(act5))
    # acc5_3 = len(set(pre5_3).intersection(set(act5))) * len(set(pre5_3).intersection(set(act5))) / (
    #         len(pre5_3) * len(act5))
    # acc5 = (acc5 + acc5_1 + acc5_2 + acc5_3) / 4
    #
    # # print("Accuracyyyyyy ", acc5)
    # # 30
    # A6 = []
    # pre6 = list(dict.fromkeys(w for s in A6 for w in s.split()))
    # A6_1 = []
    # pre6_1 = list(dict.fromkeys(w for s in A6_1 for w in s.split()))
    # A6_2 = []
    # pre6_2 = list(dict.fromkeys(w for s in A6_2 for w in s.split()))
    # B6 = []
    # act6 = list(dict.fromkeys(w for s in B6 for w in s.split()))
    # acc6 = len(set(act6).intersection(set(pre6))) * len(set(act6).intersection(set(pre6))) / (len(act6) * len(pre6))
    # acc6_1 = len(set(pre6_1).intersection(set(act6))) * len(set(pre6_1).intersection(set(act6))) / (
    #         len(pre6_1) * len(act6))
    # acc6_2 = len(set(pre6_2).intersection(set(act6))) * len(set(pre6_2).intersection(set(act6))) / (
    #         len(pre6_2) * len(act6))
    #
    # acc6 = (acc6 + acc6_1 + acc6_2) / 3

    # print("Accuracyyyyyy ", acc6)
    # print("Overall Accuracy for Unigram ::::::", (acc1+acc2+acc3)/3)

def accuracy_bigram_keyword_accuracy():
    print("---------------------------Keyword Accuracy Calculating(Bigram)-------------------------")
    print("")
    # 25
    A1 = ['ලංකාව', 'ක්රිකට්', 'බව', 'ශ්රී', 'විස්සයි', 'තරඟ', 'විස්තර', 'පරාජයෙන්']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['තරගාවලිය', 'ශ්රී', 'ලංකාව', 'ක්රීඩකයි', 'හිතාමතා', 'දුර්වල', 'ක්රීඩා', 'විලාසයක', 'නිරත', 'වුණා', 'ද', 'වැඩි']
    pre1_1 = list(dict.fromkeys(w for s in A1_1 for w in s.split()))
    A1_2 = ['දකුණු', 'අප්රිකාව', 'අප්රිකානු', 'ලංකාව', 'ක්රිකට්', 'අද', 'තරඟ', 'ක්රීඩා', 'කිරීමට', 'සහ', 'ශ්රී', 'කණ්ඩායම', 'අතර', 'විස්සයි', 'විස්ස', 'දෙවන']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['ශ්රී', 'ලංකාව', 'ක්රීඩා', 'ලෝලීන්', 'වැඩි', 'විස්තර', 'ක්රිකට්']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['නායක', 'දසුන්', 'ශානක', 'ලංකාව', 'ක්රිකට්', 'දකුණු අප්රිකාව','දුර්වල', 'ක්රීඩා', 'විලාසයක', 'විස්සයි විස්ස', 'ක්රිකට්', 'තරගාවලිය','පරාජයෙන්','විස්තර']
    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))
    acc1 = len(set(pre1).intersection(set(act1))) * len(set(pre1).intersection(set(act1))) / (len(pre1) * len(act1))
    acc1_1 = len(set(pre1_1).intersection(set(act1))) * len(set(pre1_1).intersection(set(act1))) / (
                len(pre1_1) * len(act1))
    acc1_2 = len(set(pre1_2).intersection(set(act1))) * len(set(pre1_2).intersection(set(act1))) / (
                len(pre1_2) * len(act1))
    acc1_3 = len(set(pre1_3).intersection(set(act1))) * len(set(pre1_3).intersection(set(act1))) / (
                len(pre1_3) * len(act1))
    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3) / 4
    # 26
    A2 = ['අමාත්යවරයා', 'ධූරයෙ', 'පොරොන්දු', 'සැරසෙයි', 'මහ']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම', 'අමාත්යවරයා']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['පාසල්', 'විවෘත', 'කිරීමට', 'හැකි', 'මාර්ගෝපදේශ', 'මාලාව', 'විට', 'සකස්', 'කර', 'ලබාදෙන', 'ලෙස', 'ජනාධිපති',
            'සෞඛ්යය', 'අමාත්යාංශ', 'දැනුම', 'දී', 'ඇත', 'ප්රාථමික', 'දරුවන්ට', 'තාක්ෂණ', 'අධ්යාපන', 'කටයුතු', 'සිදු',
            'කිරීමේදී', 'ගැටලු', 'මතුව', 'ඇති', 'බවද', 'වෛද්යවරු', 'මෙහිදී', 'පෙන්වා', 'තිබේ', 'අමාත්යවරයා', 'ක්රිඩා',
            'දේශීය', 'යට', 'ඇදුම', 'අවශ්ය', 'තරම්', 'දෙන්න', 'බන්දුල', 'සූදානම්']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['අමාත්යවරයා', 'ජොන්ස්ටන්ගෙන්', 'පොරොන්දු', 'මහ', 'බැංකු', 'අධිපති', 'තනතුර', 'බාරගැනීම', 'කබ්රාල්',
            'පාර්ලිමේන්තු', 'ධූරයෙ', 'අස්වී', 'සැරසෙයි', 'මිරිස්']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම', 'අමාත්යවරයා', 'මහ', 'බැංකු', 'අධිපති', 'තනතුර',
          'බාරගැනීම', 'කබ්රාල්', 'සැරසෙයි']
    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))
    acc2 = len(set(act2).intersection(set(pre2))) * len(set(act2).intersection(set(pre2))) / (len(act2) * len(pre2))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) * len(set(pre2_1).intersection(set(act2))) / (
            len(pre2_1) * len(act2))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) * len(set(pre2_2).intersection(set(act2))) / (
            len(pre2_2) * len(act2))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) * len(set(pre2_3).intersection(set(act2))) / (
            len(pre2_3) * len(act2))
    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # crime
    # print("Accuracyyyyyy ",acc2)
    A3 = ['පොලිසිය', 'කියයි', 'අත්අඩංගුව', 'ගත්', 'බව', 'කළ']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['රාජ්ය', 'අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['හිසට', 'පිස්තෝල', 'අනුරාධපුර', 'බන්ධනාගාරයේ', 'මකන්න', 'උත්සාහයක', 'සිරකරු', 'දෙදෙනෙකු', 'දණගස්වා', 'ඔවුන්ගේ', 'තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ', 'රාජ්ය', 'රත්වත්ත', 'වහා', 'අත්අඩංගුව', 'ගනු']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['අමාත්යවරයා', 'විමලවීර', 'හූ', 'කියා']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['සිරකරු', 'දෙදෙනෙකු','බන්ධනාගාරයේ','තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ','බන්ධනාගාර','අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත','අත්අඩංගුව']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))
    acc3 = len(set(act3).intersection(set(pre3))) * len(set(act3).intersection(set(pre3))) / (len(act3) * len(pre3))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) * len(set(pre3_1).intersection(set(act3))) / (
            len(pre3_1) * len(act3))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) * len(set(pre3_2).intersection(set(act3))) / (
            len(pre3_2) * len(act3))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) * len(set(pre3_3).intersection(set(act3))) / (
            len(pre3_3) * len(act3))
    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    TP = 0
    FP = 0
    TH = 0.3

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

    BPrecision = (TP / (TP + FP))

    print("Overall Precision for Bigram ::::::", BPrecision)

    # print("Accuracyyyyyy ", acc6)
    # print("Overall Accuracy for Bigram ::::::", (acc1 + acc2 + acc3 ) / 3)

# coding=utf-8

def accuracy_trigram_keyword_accuracy():
    print("---------------------------Keyword Accuracy Calculating(trigram)-------------------------")
    print("")
    # Considering Sports
    A1 = ['විස්ස', 'තරඟ', 'ක්රීඩා', 'කරන', 'ශ්රී', 'ලංකාව']
    pre1 = list(dict.fromkeys(w for s in A1 for w in s.split()))
    A1_1 = ['ශ්රී', 'ලංකාව', 'ක්රිකට්', 'බව', 'වැඩි', 'විස්තර', 'පරාජයෙන්', 'පසු']
    pre1_1 = list(dict.fromkeys(w for s in pre1 for w in s.split()))
    A1_2 = ['තරගාවලිය', 'ශ්රී', 'ලංකාව', 'ක්රීඩකයි', 'හිතාමතා', 'දුර්වල', 'ක්රීඩා', 'විලාසයක', 'නිරත', 'වුණා', 'ද',
            'වැඩි', 'විස්තර']
    pre1_2 = list(dict.fromkeys(w for s in A1_2 for w in s.split()))
    A1_3 = ['ලංකාව', 'කණ්ඩායම', 'තෙවන', 'විස්සයි']
    pre1_3 = list(dict.fromkeys(w for s in A1_3 for w in s.split()))
    B1 = ['නායක', 'දසුන්', 'ශානක', 'ශ්රී ලංකාව', 'ක්රිකට්', 'දකුණු අප්රිකාව', 'විස්සයි විස්ස', 'ක්රිකට්', 'තරගාවලිය',
          'පරාජයෙන්']
    act1 = list(dict.fromkeys(w for s in B1 for w in s.split()))
    acc1 = len(set(act1).intersection(set(pre1))) * len(set(act1).intersection(set(pre1))) / (len(act1) * len(pre1))
    acc1_1 = len(set(pre1_1).intersection(set(act1))) * len(set(pre1_1).intersection(set(act1))) / (
            len(pre1_1) * len(act1))
    acc1_2 = len(set(pre1_2).intersection(set(act1))) * len(set(pre1_2).intersection(set(act1))) / (
            len(pre1_2) * len(act1))
    acc1_3 = len(set(pre1_3).intersection(set(act1))) * len(set(pre1_3).intersection(set(act1))) / (
            len(pre1_3) * len(act1))
    acc1 = (acc1 + acc1_1 + acc1_2 + acc1_3) / 4

    A2 =  ['ජොන්ස්ටන්ගෙන්', 'පොරොන්දු', 'අධ්යාපන', 'ඇමැතිගෙන්', 'සාමාන්', 'පෙළ', 'සිසුන්', 'විශේෂ', 'නිවේදනයක්', 'මහ', 'බැංකු', 'අස්වී', 'සැරසෙයි', 'අමාත්යවරයා', 'ජොන්ස්ටන්', 'ජනතාවට', 'දුන්', 'රාජ්ය', 'මන්ත්රී', 'කමෙන්', 'ඉල්ලා','අස්වෙයි', 'ලිපිය', 'ලබන', 'සතියේ', 'පාසල්', 'විවෘත', 'දී', 'තිබේ', 'මිරිස්', 'ආනයන', 'කෘෂිකර්ම', 'ක්රිඩා','ඇමතිගේ', 'ජොබ්', 'එක', 'කරන්න', 'ඔනේ', 'එකට්යි', 'එපා', 'එකටයි', 'හැම', 'මගුලකටම', 'හොම්බ', 'දානවා', 'දන්න','මගුලකුත්', 'නැහැ', 'මේ', 'වෙලාවෙ', 'භාණ්ඩ', 'හංගන', 'වෙළෙන්දො', 'හරිය', 'එදා', 'සුනාමි', 'වෙලාවේ', 'චේන්','කඩපු', 'හොරු', 'වගේ', 'රෝහිත', 'ලංකාවේ', 'බ්රෑන්ඩ්', 'තියෙනවා', 'ඕන', 'නං', 'සතොසෙන්', 'දෙන්නම', 'වෙළද', 'බය',
         'වෙන්න', 'කියයි', 'දේශීය', 'යට', 'බන්දුල', 'සූදානම්']
    pre2 = list(dict.fromkeys(w for s in A2 for w in s.split()))
    A2_1 = ['මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම', 'අමාත්යවරයා']
    pre2_1 = list(dict.fromkeys(w for s in A2_1 for w in s.split()))
    A2_2 = ['ජොන්ස්ටන්ගෙන්', 'පොරොන්දු', 'අමාත්යවරයා', 'අස්වී', 'සැරසෙයි', 'මහ', 'බැංකු']
    pre2_2 = list(dict.fromkeys(w for s in A2_2 for w in s.split()))
    A2_3 = ['අමාත්යවරයා', 'ජොන්ස්ටන්ගෙන්', 'පොරොන්දු', 'මහ', 'බැංකු', 'අධිපති', 'තනතුර', 'බාරගැනීම', 'කබ්රාල්', 'පාර්ලිමේන්තු', 'ධූරයෙ', 'අස්වී', 'සැරසෙයි', 'කෘෂිකර්ම', 'මිරිස්', 'ආනයන']
    pre2_3 = list(dict.fromkeys(w for s in A2_3 for w in s.split()))
    B2 = ['මිරිස්', 'ආනයන', 'සම්පුර්ණ', 'නතර', 'කරනවා', 'කෘෂිකර්ම', 'අමාත්යවරයා','මහ', 'බැංකු', 'අධිපති', 'තනතුර', 'බාරගැනීම', 'කබ්රාල්','සැරසෙයි']
    act2 = list(dict.fromkeys(w for s in B2 for w in s.split()))
    acc2 = len(set(act2).intersection(set(pre2))) * len(set(act2).intersection(set(pre2))) / (len(act2) * len(pre2))
    acc2_1 = len(set(pre2_1).intersection(set(act2))) * len(set(pre2_1).intersection(set(act2))) / (
                len(pre2_1) * len(act2))
    acc2_2 = len(set(pre2_2).intersection(set(act2))) * len(set(pre2_2).intersection(set(act2))) / (
            len(pre2_2) * len(act2))
    acc2_3 = len(set(pre2_3).intersection(set(act2))) * len(set(pre2_3).intersection(set(act2))) / (
            len(pre2_3) * len(act2))
    acc2 = (acc2 + acc2_1 + acc2_2 + acc2_3) / 4

    # crime
    # print("Accuracyyyyyy ",acc2)
    A3 = ['අනුරාධපුර', 'බන්ධනාගාරයේ', 'මකන්න', 'උත්සාහයක', 'සිරකරු', 'දෙදෙනෙකු', 'දණගස්වා', 'ඔවුන්ගේ', 'හිසට', 'පිස්තෝල', 'තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ', 'රාජ්ය', 'අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත', 'වහා', 'අත්අඩංගුව', 'ගනු']
    pre3 = list(dict.fromkeys(w for s in A3 for w in s.split()))
    A3_1 = ['කළ', 'බව', 'කියන', 'බන්ධනාගාර', 'රාජ්ය', 'අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත', 'මහ', 'රෑ', 'කඩා', 'පැන', 'පිස්සු', 'කෙලපු', 'අනුරාධපුර', 'බන්ධනාගාරයේ', 'මකන්න', 'උත්සාහයක', 'මේ', 'වනවිට', 'කළමනාකරණ', 'සහ', 'සිරකරු', 'පුනරුත්ථාපන', 'ධූරයෙ', 'ඉල්ලා', 'අස්වී', 'තිබෙන', 'මහතා', 'තවදුරටත්', 'මැණික', 'ස්වර්ණාභරණ', 'ධූරයේ', 'කටයුතු']
    pre3_1 = list(dict.fromkeys(w for s in A3_1 for w in s.split()))
    A3_2 = ['අමාත්යවරයා', 'ලොහාන්', 'රත්වත්ත']
    pre3_2 = list(dict.fromkeys(w for s in A3_2 for w in s.split()))
    A3_3 = ['අත්අඩංගුව', 'ගත්', 'බව']
    pre3_3 = list(dict.fromkeys(w for s in A3_3 for w in s.split()))
    B3 = ['සිරකරු', 'දෙදෙනෙකු', 'බන්ධනාගාරයේ', 'තබා', 'මරාදමන', 'බවට', 'තර්ජන', 'කළ', 'බන්ධනාගාර', 'අමාත්යවරයා',
          'ලොහාන්', 'රත්වත්ත', 'අත්අඩංගුව']
    act3 = list(dict.fromkeys(w for s in B3 for w in s.split()))
    acc3 = len(set(act3).intersection(set(pre3))) * len(set(act3).intersection(set(pre3))) / (len(act3) * len(act3))
    acc3_1 = len(set(pre3_1).intersection(set(act3))) * len(set(pre3_1).intersection(set(act3))) / (
            len(act3) * len(act3))
    acc3_2 = len(set(pre3_2).intersection(set(act3))) * len(set(pre3_2).intersection(set(act3))) / (
            len(act3) * len(act3))
    acc3_3 = len(set(pre3_3).intersection(set(act3))) * len(set(pre3_3).intersection(set(act3))) / (
            len(act3) * len(act3))
    acc3 = (acc3 + acc3_1 + acc3_2 + acc3_3) / 4

    TP = 0
    FP = 0
    TH = 0.3

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

    TPrecision = (TP / (TP + FP))

    print("Overall Precision for Trigram ::::::", TPrecision)

    # print("Overall Accuracy for Trigram ::::::", (acc1 + acc2 + acc3) / 3)





# driver code
if __name__ == '__main__':
    print(" ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Long Term Trends - Precision  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(" ")
    accuracy_unigram_keyword_accuracy()
    print(" ")
    accuracy_bigram_keyword_accuracy()
    print(" ")
    accuracy_trigram_keyword_accuracy()
    print(" ")