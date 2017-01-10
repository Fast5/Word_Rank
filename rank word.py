def split_words(source):
    source = split_string(source, ",.#:").replace("\n", "")
    splited_words = source.split()
    
    from nltk.corpus import wordnet as wn
    word_prototype = []
    for e in splited_words:
        word = wn.morphy(e)
        if word != None:
            word_prototype.append(word)
        
    #print source
    return word_prototype

def split_string(source,splitlist):
    result= []
    atsplit= True
    for char in source:
        if char in splitlist:
            atsplit= True
        else:
            if atsplit:
                result.append(char)
                atsplit= False
            else:
                result[-1] = result[-1] + char

        
    return "".join(result)


def count_words(list_of_words):
    ranks = {}
    for word in list_of_words:
        if not word in ranks:
            ranks[word] = 1
        else:
            ranks[word] = ranks[word] + 1

    return ranks


def sort_rank(ranks):
    return sorted(ranks.iteritems(), key=lambda d:d[1], reverse = True)

def rank_word():
    
    # 英文文本位置
    paragraph_location = "passage.txt"   
    
    source = open(paragraph_location, "r")

    #print source.read()
    # 分割文本成单个单词
    # “This is an exmaple” ==> ["This", "is", "an", "example"]
    list_of_words = split_words(source.read())
    
    # 计算每个单词的出现次数
    ranks = count_words(list_of_words)
    
    # 根据单词出现的频率排序
    ranked_words = sort_rank(ranks)
    
    # 输出到excel文件
    import pandas as pd
    rankData = pd.DataFrame(ranked_words, columns = ['Word', 'Frequency'])
    #print rankData
    rankData.to_excel("Result.xls", index = True, header = True)

    source.close()

rank_word()

def test():
    sentence = "It is a test."
    assert split_words(sentence) == ["It", "is", "a", "test"]
    assert count_words(["It", "is", "a", "test", "test"]) == {"test": 2, "a": 1,
                                                              "is": 1, "It": 1}
#    assert sort_rank(count_words(["It", "is", "a", "test", "test", "a", "a"])) =={
#        "a": 3, "test": 2, "is": 1, "It": 1}

    print ("All tests passed.")

#test()
