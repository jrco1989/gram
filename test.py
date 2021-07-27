
if __name__ == '__main__':
    def test (arr,word):
        response = [arr.count(word)]
        response.append(len(arr))
        print(response)
        return response


    test(["ab","a"], "a")