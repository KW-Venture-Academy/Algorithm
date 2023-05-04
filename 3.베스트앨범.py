#3.베스트앨범
def solution(genres, plays):
   answer = []
   genre_play = {}
   for i in range(len(genres)):
       if genres[i] not in genre_play:
           genre_play[genres[i]] = plays[i]
       else :
           genre_play[genres[i]] += plays[i]
   song_infos = {}
   for i in range(len(genres)):
       if genres[i] not in song_infos:
           song_infos[genres[i]] = [(plays[i], i)]
       else:
           song_infos[genres[i]].append((plays[i], i))
   sorted_genre_play = sorted(genre_play.items(), key = lambda x : x[1], reverse = True)

   for genre, total_play in sorted_genre_play:
       song_list = sorted(song_infos[genre], key=lambda x: (-x[0], x[1]))
       for i in range(min(len(song_list), 2)):
           answer.append(song_list[i][1])
   return answer
