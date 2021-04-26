def MassVote(N, Votes):
    sum_votes = round(sum(Votes) * 0.5, 3)
    max_votes = max(Votes)
    cnt_max = Votes.count(max_votes)

    if cnt_max == 1:
        if max_votes > sum_votes:
            return 'majority winner ' + str(Votes.index(max_votes) + 1)
        elif max_votes <= sum_votes:
            return 'minority winner ' + str(Votes.index(max_votes) + 1)
    return 'no winner'


#Votes = [5, 10, 10, 15, 60]
#N = 3
#print(MassVote(N, Votes))
