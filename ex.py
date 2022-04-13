from jooxdl import rs
def main(args):
    a=rs(args,debug=False,debug_lang="th")
    til=a.main()
    print(til)
    
if __name__ == '__main__':
    main('https://open.joox.com/s/rd?k=rq3UP')
    #https://open.joox.com/s/rd?k=rqyKd
    #https://open.joox.com/s/rd?k=rq3UP
#{'album_id': 'paOOJWjuOQbr03FsrDlM2g==', 'id': 'K016UIbdJj0iG1OAZZX_Bw==', 'name': 'Morning', 'album_name': 'Morning - Single [JOOX Exclusive]', 'artist_list': [{'id': 'VHbqozs8i0kurBMEuzLrcw==', 'name': 'LAZYLOXY'}], 'play_duration': 232, 'images': [{'width': 1000, 'height': 1000, 'url': 'https://image.joox.com/JOOXcover/0/4b928564a4359e64/1000'}, {'width': 300, 'height': 300, 'url': 'https://image.joox.com/JOOXcover/0/4b928564a4359e64/300'}, {'width': 100, 'height': 100, 'url': 'https://image.joox.com/JOOXcover/0/4b928564a4359e64/100'}], 'vip_flag': 0, 'is_playable': True, 'track_free_action_control': 35}