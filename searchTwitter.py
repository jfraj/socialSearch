import sys
import twitter


def get_tweeter_auth_info_dic(fname = 'tweeter_auth_info.txt'):
    '''
    Returns dictionary with parameters to connect to tweeter
    the file it reads the info from must be in the format (space before value)
    CONSUMER_KEY <value>
    CONSUMER_SECRET <value>
    OAUTH_TOKEN <value>
    OAUTH_TOKEN_SECRET <value>
    More info about the keys here: https://apps.twitter.com/app/7077114/keys
    '''
    info_dic = {}
    auth_info_file = open(fname)
    for iline in auth_info_file.readlines():
        iline = iline[:-1]##Exclude the \n
        isplit = iline.split(' ')
        info_dic[isplit[0]] = str(isplit[1])
    return info_dic

def search_twitter(searchTerm, count=100):
    '''
    Returns a list of 'count' tweet dictionary with info for the given searchTerm
    searchTerm can be either #hastag or @user (maybe other options, need to be checked)
    '''
    #See https://dev.twitter.com/docs/api/1.1/get/search/tweets
    auth_info_dic = get_tweeter_auth_info_dic()
    ##Connect to twitter
    #auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    auth = twitter.oauth.OAuth(auth_info_dic['OAUTH_TOKEN'], auth_info_dic['OAUTH_TOKEN_SECRET'], auth_info_dic['CONSUMER_KEY'], auth_info_dic['CONSUMER_SECRET'])
    twitter_api = twitter.Twitter(auth=auth)

    search_results = twitter_api.search.tweets(q=searchTerm, count=count)

    statuses_list = search_results['statuses']
    out_tweet_list = []
    for itweet_dic in statuses_list:
        #print '\n--------------'
        #print itweet_dic['user']['name']
        #print '(@{0})'.format(itweet_dic['user']['screen_name'])
        #print itweet_dic['text']
        iout_dic = {'name': itweet_dic['user']['name'], 'screen_name': itweet_dic['user']['screen_name'], 'text': itweet_dic['text']}
        out_tweet_list.append(iout_dic)
    #print 4*'\n'
    return out_tweet_list

def show_twitter_search(searchTerm, count=10):
    '''
    Print out the twitter search results
    for testing the search
    '''
    print 'Searching twitter for {0}\n'.format(searchTerm)
    tweet_list = search_twitter(searchTerm, count)
    #print tweet_list
    for itweet_dic in tweet_list:
        print itweet_dic['name']
        print '(@{0})'.format(itweet_dic['screen_name'])
        print itweet_dic['text']
        print 10*'-'+'\n'

if __name__=='__main__':
    '''
    For testing you can type the command:
    python searchTwitter.py <search term: #hastag or @name> <counts>
    (options are optional)
    search term must be between quotation marks 
    '''
    search4 = '#mtl'
    count4 = 5
    print sys.argv
    if len(sys.argv) > 1:
        search4 = str(sys.argv[1])
    if len(sys.argv) > 2:
        count4 = int(sys.argv[2])
    #show_twitter_search('#mtl', 5)
    show_twitter_search(search4, count4)
    #print get_tweeter_auth_info_dic()
