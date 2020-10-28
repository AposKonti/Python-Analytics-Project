import urllib.request
import os

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SECTION 1
change_char_place = []
path = os.path.dirname(os.path.realpath(__file__))
for i in range( len(path) ):
    if path[i] == "\\":
        change_char_place.append(i)
path = list(path)
for i in change_char_place:
    #print(i)
    path[i] = "/"
path = "".join(path)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END SECTION 1



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SECTION 2
#final quarter 2011 link
url2011 = 'https://www.statistics.gr/en/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113865&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=en'
#final quarter 2012 link
url2012 = 'https://www.statistics.gr/en/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113886&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=en'
#final quarter 2013 link
url2013 = 'https://www.statistics.gr/en/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113905&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=en'
#final quarter 2014 link
url2014 = 'https://www.statistics.gr/en/statistics?p_p_id=documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-2&p_p_col_count=4&p_p_col_pos=2&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_javax.faces.resource=document&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_ln=downloadResources&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_documentID=113925&_documents_WAR_publicationsportlet_INSTANCE_VBZOni0vs5VJ_locale=en'
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END SECTION 2


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>SECTION 3
#download of above xls fils
urllib.request.urlretrieve(url2011, path + "/2011.xls")
urllib.request.urlretrieve(url2012, path + "/2012.xls")
urllib.request.urlretrieve(url2013, path + "/2013.xls")
urllib.request.urlretrieve(url2014, path + "/2014.xls")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END SECTION 3