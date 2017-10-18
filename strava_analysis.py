import authorize
import location_park
import datetime
import time
#import challenge
username= "YOUR USERNAME HERE"
#type ="Ride"
#activities = []
start=datetime.datetime(2017,1,1)


def start_challenge(competitor_id, client):
	frnd_activity= client.get_friend_activities()
	competitor_dist=0.00
	for friend in frnd_activity:
		if friend.athlete.id==competitor_id:
			competitor_dist+=float(friend.distance)

	print('Competitor distance= ', competitor_dist)
	return competitor_dist

def get_locations(client):
    activities= client.get_friend_activities()
    start_locations=[]
    corresponding_id=[]
    summary_locations=[]

    for run in activities:
        start_locations.append(run.start_latlng)
        corresponding_id.append(run.athlete.id)  


    print("Locations", start_locations)
    print("IDs", corresponding_id)


def decide_winner(competitor_dist, client):
    user_activities= client.get_activities()
    user_dist=0.0
    #for activity in user_activities:
     #   user_dist+=float(activity.distance)
      #  lat_lng= activity.start_latlng
       # print("Lat_Lng", lat_lng)

    if (user_dist>competitor_dist):
        print('Congrats! You won the challenge! You ran ',user_dist, 'm, your competitor ran ',competitor_dist, 'm')	
        return 1

    elif(user_dist<competitor_dist):
        print('Sorry, You lost the challenge. You ran ',user_dist, 'm , while your competitor ran ',competitor_dist, 'm')
        return 2
    else:
        print("It's a tie!. You both ran ", user_dist, "metres!")
        return 3


def main():

    """Manual Testing of Scrubbing"""
    client = authorize.get_authorized_client(username)
    #act_manager = ActivityManager(client)
    athlete = client.get_athlete()
    #athlete_2=client.get_athlete(7655679)
    #print(athlete_2.firstname, 'ran ', athlete_2.)
    #frnd_activity= client.get_friend_activities()
    #dist=0.00
    #for activity in frnd_activity:
    	#if activity.athlete.id==7655679:
    #	print('Athlete ID:', activity.athlete.id, 'Name:', activity.name, activity.distance)
    #	dist+=float(activity.distance)
    #print('Total distance= ', dist)	
    start=input('Type c to start a challenge, or p running places near you')
    start=start.lower()

    if start=='c':
        friend_name=[]
        friend_ID=[]
        friends=client.get_athlete_friends()
        for friend in friends:
            friend_name.append(friend.firstname)
            friend_ID.append(friend.id)

        for i in range(0,len(friend_name)):
            print(friend_name[i],friend_ID[i], i)

        competitor= input('Enter the corresponding number for the competitor of your choice')
        competitor=int(competitor)
        competitor_id=friend_ID[competitor]
       # time.sleep(10) #Use this for testing
        athlete2_dist=start_challenge(competitor_id, client)
        #time.sleep(60*60*24*30) #Sleep for 30 days before checking for winner 
        winner=decide_winner(athlete2_dist,client)
        get_locations(client)

    if start=='p':
        get_locations(client)
         

    #client.deauthorize()
if __name__ == "__main__":
    main();    