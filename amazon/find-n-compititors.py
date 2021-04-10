import collections
def findNcompititors(numCompetitors,topNCompetitors,competitors,numReviews,reviews):
    dt = collections.defaultdict(int,{i for i in competitors})
    # for i in competitors:
    #     dt[i] = 0
    for review in reviews:
        # temp = review.lower()
        # #print(temp)
        for i in competitors:
            if i in review.lower():
                dt[i]+=1
                break
    print(dt)
    res = sorted(dt, key=lambda x: (-dt[x], x))[:topNCompetitors]
    return res

if __name__ == "__main__":
    numCompetitors=6
    topNCompetitors = 7
    competitors = ["newshop", "shopnow", "afashion", "fashionbeats", "mymarket", "tcellular"]
    numReviews = 6
    reviews = [
    "newshop is providing good services in the city; everyone should use newshop",
    "best services by newshop",
    "fashionbeats has great services in the city",
    "I am proud to have fashionbeats",
    "mymarket has awesome services",
    "Thanks Newshop for the quick delivery"]
    print(findNcompititors(numCompetitors,topNCompetitors,competitors,numReviews,reviews))

# Output
# ["newshop", "fashionbeats"]