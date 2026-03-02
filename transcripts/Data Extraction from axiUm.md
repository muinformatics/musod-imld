**Data Extraction from axiUm-20260205_100244-Meeting Recording**

February 5, 2026, 4:02PM

59m 29s

<img src="media/ell80jpgigyfipzrmjypp.png" style="width:0.22917in;height:0.22917in" />**  
Keller, Stacy** started transcription

<img src="media/tbj971ol9jkgt_fjx0vdu.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 0:08  
Give me just a moment here. I'm gonna. I'm just opening up a folder to get access to who's uncovering here.  
Alright, good. Thanks everybody. I'm gonna just share my screen.  
So what we're going to be covering here is pulling data out of Axiom and today we're we might not even get into any of the data that I have a lot of background information in terms of.

<img src="media/ouqgdhisowpp12l1a0zci.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 1:03  
OK.

<img src="media/6hhadgmsmo6avs6qqtf69.png" style="width:0.30208in;height:0.30208in" />**  
Keyes, Tom** 1:10  
Yeah.

<img src="media/ax3jasts0znikmtqosjkv.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 1:17  
Kind of where you can find things, where some things are stored. But I do have here a list of, and I'll show you shortly where this is, kind of a list of the topics that we'll cover is kind of the people where they are in Axiom and where we can find them.  
Some known issues with how that is done in there, how Axiom organizes some locations, the maintenance area. The Info Manager is a reporting system within Axiom.  
Then there's a whole area of information for clinical treatment, scheduling, lab tracking, dispensary, financial and evaluations.  
These are very broad topics. We might get into the people part of it today. So what I'm hoping to do is as I show you some of the tools that we can use, I will try to come up with some queries or some.  
Questions that you can turn to use these tools, try to pull the information and you're going to start to get a sense of some of the challenges in there. And I'm going to ask that that you develop some things separately, so we're going to bring them back and compare.  
Did we all get the same answer? Well, how did we find that type of thing?

<img src="media/znckzcqkzs7vdn1fttwzs.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 2:33  
Yes.

<img src="media/yfoqvvf9bbiloyxriygkh.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 2:38  
So maybe before we begin, does that, does that make sense of of what we're covering? Does anybody have questions about that?

<img src="media/36qggfgqaiyvgneqxzgea.png" style="width:0.30208in;height:0.30208in" />**  
Keyes, Tom** 2:47  
Makes sense.

<img src="media/l5706ezonxtcddb-vgrkj.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 2:47  
Um.  
So let me start with the resources and the place where you're going to find most of this is in the Informatics area, Administration, Axiom, the technical documentation. So let me just show you that. So in other words, I'm going to come back to just the Informatics area.  
So in Informatics under administration there is an Axiom folder. Within the Axiom folder I have technical documentation.  
And that's where, uh.  
And that's where much of this data is. This one that I'm talking about here, Axiom database topics, that's that's Word document that I'm working from now. So let me go back to the Word document.  
Also within that area that Axiom has a a database table dictionary. Let me show you that.  
That would be the one I have used often.  
Is an older version, and I'll show you why in a minute when I find it. Actually, I'll show it on here.  
I've got it highlighted in line. It is a data dictionary from version 6 because this is the last time Axiom was doing it this way. So yeah, I know it's outdated, but this is where I'll start with.  
Within this.

<img src="media/wqf3vbm69uhtssw3sngcp.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 4:32  
OK.

<img src="media/vgiabrz9k1gxvprd6lf6t.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 4:32  
Area are all of the tables and I I I think at last count it's over 600 tables exist in in Axiom.  
Let's take the appointment table. When I go into that, it'll take me to a schema of the appointment and show me the fields, the type of the field, and a brief description of it. It's this is very rudimentary what they have here.  
Let me just show you again. I'm going to come back up to.

<img src="media/okgo2b7_zmqcqxswdwh3n.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 5:03  
So quick question, this is something they generate for us or we've extrapolated that?

<img src="media/zy3rdont7nkjbdpaqmaix.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 5:04  
Yes.  
It is something that they generate and.

<img src="media/sbq-9bu5p-5flcfa8q6ev.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 5:13  
OK. Thank you.

<img src="media/ocqaaqsooxp5uz85wdkij.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 5:17  
Recently, because I I do have the latest version, I'm going to show you that we it's not up on their portal, which I'm going to show you in a little bit as well. We had to ask for this in a case request.  
And they went through a number of questions that I have to kind of say, yes, I understand this. Basically we're saying we will not share this with anybody, but it but it's not easily available for their portal. You do have to ask that. So we're currently on this data dictionary 2024.  
I'm gonna open it up and what you'll see here is in a similar format. Here's all of the different tables in order. We just looked at that appointment one.  
And then here's the listing. I just wanted to show you the two versions that existed. You certainly can work from this one. Sometimes I find things a little easier to find and search in the spreadsheet, but the current one.

<img src="media/352v5l0wcllollo_zov1g.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 6:20  
OK.

<img src="media/jkwxpzp032hxrfbult0go.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 6:22  
Is this HTML file that exists out there? There's a lot more to explain in terms of this is this isn't the only place where you can turn to, but it is part of the limited information that they give us is this data dictionary.

<img src="media/sxtywlpwuawhr8p6glvus.png" style="width:0.30208in;height:0.30208in" />**  
Keyes, Tom** 6:31  
Yeah.

<img src="media/sdwmlgsw5xozty_ou9ufe.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 6:39  
Don't we only have access to like 30 tables too under the staging database?

<img src="media/x4d0ikwyeeroz-yx9kglq.png" style="width:0.30208in;height:0.30208in" />**  
Keyes, Tom** 6:40  
OK.

<img src="media/e8tkszejdvqgijci4nnh6.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 6:44  
The staging database right only has about 30 of the tables. The live database has all all of them.

<img src="media/zgb5z7k6zrslyf9h1bi9r.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 6:51  
OK.

<img src="media/c8-wtcixa5jnofl3nezrz.png" style="width:0.30208in;height:0.30208in" />**  
Keller, Stacy** 6:52  
Can I just interrupt real quick? Kaden, somebody is here about an installation that they were emailing you about.

<img src="media/gzgh9hwo47rb67yx--qds.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 7:01  
Um.  
That's weird. I'll have to. I'll have to drop out of the meeting to talk to this guy.

<img src="media/k9gd0_e9xcdrlboorljgp.png" style="width:0.30208in;height:0.30208in" />**  
Keller, Stacy** 7:08  
OK.

<img src="media/harv4dl2r9hogcvefa4ck.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 7:10  
OK.

<img src="media/at7fczumiwjieyfrhpfla.png" style="width:0.30208in;height:0.30208in" />**  
Keller, Stacy** 7:11  
Thank you.

<img src="media/psrvmgpb17reon4dh8l7n.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 7:12  
Mm.  
So that we we talked a bit about the database table dictionary.  
Then there's also the entity relationship diagrams. Those exist here as well, and I'll show you.  
Here is the entity relationship diagrams for in 2024.  
And bookmarked on the side are some general categories of things.  
If I look in the appointment areas.

<img src="media/jit5dl8jcw-x1ijhp9ion.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 7:57  
Yeah.

<img src="media/dgh5z7afethny7k_e8avr.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 7:59  
Now I can see the relationships between the tables, so this is helpful to at least get a sense of relationships that do exist between the tables.  
The thing that is missing that I've asked Exan, if they have a workflow to tell me when they create an appointment, what's the process that gets affected? Are there? Are there certain tables that get created?  
Or you know that so that information is not available to us. They this is the only thing that they're providing is these dictionaries and these relationship tables, but the rest they don't give out to the school.  
I've asked them if they can provide some training to us. We've asked them several times over the years and they tell us that they don't because all the schools are different. So they would leave that up to the schools to figure out training and to figure out how to use and pull information for Max.  
The last time I asked was about two years ago. So if it's changed since then, I'm not sure, but I probably asked them five or six times over the last 20 years and that's the response from them. So the two we've looked at so far would be this data dictionary and then these entity relationship diagrams.  
Then there are also a number of documents out here as well.  
And what I've been storing here is just, uh, maybe some of the different setup guides. It is not all of them. Um.  
But I'll show you in a little bit where you can get to the portal to get access to more or all of the information from AX. Again, this is the location you want to take a look at for some of this information.  
So I've been referring to this Exxon portal.  
We'll open it up.  
You would work with Terry to have him make a request to get you added to the portal.  
And once you're in the portal, here's a place where we can submit cases. Usually Terry will be the one submitting the cases, and that's something that we have to decide here of who might, you know, whether you should also be someone to submit a case or whether that should go through Terry.  
But the important thing here is here's where you can find some documents. We don't typically deal with the setup guides. That would be Terry and ITS, but we may be interested in the user guides and some of the tech documents. You can also search for something, so if I want to come here.  
It'll come up a list with. It's not like a Google search that it's going to give you the best answer to all this first, so you might have to look a little bit to find it. This might really be what I'm looking for is this user guide and when you come into it now I have the ability to download it.  
Sometimes they'll have multiple versions. We are currently on version 2024, so then that would be the appropriate one to download from there.

<img src="media/wzq756gp-zjcdso5w4lij.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 11:33  
OK.

<img src="media/jam61cza-qpfunkdxgo28.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 11:35  
Another good resource is this consortium.edr.  
Yeah.  
I I think I've mentioned to many of you that this this consortium is the one who has the mid-year meetings. I find there that meeting has been the most.  
I've found most beneficial because many of many of the people who attend from the technology side are the people who are pulling the data or configuring the data. So there's a lot of good technical discussion at at this meeting they also have.  
Discussion groups. So once you're in there and you and you log in, you can indicate which areas to join for a listserv. And so like I'm on the technology one, so I will get messages from that listserv.  
Couple times a week so you get a sense of what some of the other places are looking for, but I'd strongly encourage it at least join the discussion group and maybe touch base with Tom in terms of can I attend this midyear meeting.  
So that you can meet with some of the other professionals, technology professionals who are working with Nexing. It's a great, great resource. So that was this one. So again, the discussion groups are important and I think that major meeting is helpful.  
Now let's talk a little bit about the databases. So some of the terminology here I'll it's use it in a few different ways. There is an Axiom database for production. It's Oracle based.  
There's an Axiom database for training. It's Oracle based in an Axiom database, and this is one that's we've called it dev and stage.  
That is also in Oracle, so all three of these are Oracle databases.  
The production is the one that is used in the clinics. The training is used mostly in the SIM lab and in some other places for the pre-doc students before they're in the clinical area. So pre-clinical, they're not really seeing the patient.  
But that's where they can simulate some of their exercises. So that's the training database. Training is not a it's it's it's not a current copy of live. It's a copy from probably 1012 years ago.  
It got separated and we've never refreshed training from that point on and then we used it more just for cases in the in the.  
In the SIM lab or in that preclinical setting. So when Terry makes updates to Axiom, he should be applying the same updates to Axiom training so that they are similar environments, but they're not copies of each other.  
Axiom Production and Axiom Dev are very close. They'll often refresh dev from production. They'll work out and reach out to us. There's about four or five of us who are working in the development database.  
And they'll kind of negotiate a time to say, hey, next week, Monday, we're going to refresh the dev database, basically making a copy of production to dev. What ITS uses it for is to do the work to.  
Test out a new upgrade, test out a certain feature. Once it's tested and reviewed by us and approved in the dev database, then they'll apply that same change in the production area. So the dev is a good place for us to turn to test things out and to check things out because it is a.  
Very close copy of production, but those are the three different databases and it's helpful or important to remember these three are Oracle databases.  
Now there's another database Kaden was referring to earlier and this is the the staging database. We'll ask access that through Microsoft SQL because it is a.  
Um.  
Each night the data, some of the data from Axiom is pulled and updated into this database. It's only about 30 tables. It's the tables that we use mostly for the dashboard and.  
Those tables represent probably 95% of the tables used as we pulled some things. It is a, like I said, that small subset of tables, but there's an important feature with this is that.  
It is not a dump every night from production into the BI staging and this I discovered as we started using it. Blake Ward is the person over in ITS who.  
Handles and manages this staging database and on a per table basis he developed rules for updating the table based on live.  
So he made assumptions about each table and um.  
Now let's so let's just take in a table. Let's say a point is there yesterday.  
We consider the appoint table in our.  
Staging area up to date. Today we go into Axiom and we added five appointments and modified 5 appointments at the end of the day. But what his extraction process looks for is.  
Changes and brings those over. Now some tables he may bring over completely, but other tables he may just do it on that looking for the modified and.  
What happened to what we discovered is that.  
Hexan used different.  
Methods and different ways of recording when they modified or which ones they did. So it took about a month or two that we continued to discover that there was something missing from our staging database that seems to have settled down after the first three to six months.  
But I do not have a way for me to guarantee that everything that's in that staging database is is accurate.  
So that that's a qualification that I put out there is that I don't know the process that.  
Lake is using it on every table to bring that over, so that's something to keep in mind is if we're if you are finding some discrepancies for a way to ensure that it's possible the staging database.  
Is not 100% accurate because of the extraction process.  
The credentials for the database. Oh, sure, go ahead. Yeah, go ahead.

<img src="media/ptvmdiqlcsuuddjocszfk.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 19:21  
Quick question for you real real quick that the BI is, is that a hard link to Power BI or does that just stand for the generic business intelligence?

<img src="media/hnpap6qhm4tvuhojramk0.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 19:35  
Let me let me just see on this one. I'm I'm gonna open up my SQL server. I think I'm just using the name that they have from database.

<img src="media/owdd6qxps7pb2z1vxttgz.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 19:47  
OK. So it's probably doing just general business intelligence and not specific to Power BI. All right. Thank you.

<img src="media/hblghn937aoqdneujjhfz.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 19:54  
Yeah, because I I don't think that we can access it through Power BI or that it might be a special configuration, but but I was just using the terminology they used for the name of the connection. Yeah, see.

<img src="media/f4q1ggfljjkpaza8ptukx.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 20:03  
OK.

<img src="media/1plxqcshgcqqvqht2bgpn.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 20:05  
This this is their their name of the BI database here.

<img src="media/8zhgntixbd4te-6zdy9w1.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 20:05  
Thank you.

<img src="media/rebv9llpars2d-36-oicr.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 20:13  
Um.  
And then credentials exist in the password state. I think that you all know how to get to that. If not, just touch base with me. But within the password state there is an Informatics folder. Within the Informatics folder are the different.  
Databases or areas that that you would be connected to and I think the names of the servers would be listed there.  
I'm I'm gonna go past the databases now if unless there are more questions.  
OK, this apps section to me would be the different tools that are available for us to access the information from Axiom.  
So one is the Axiom Infomatic.  
I'm gonna start to launch Axiom. It'll take a little bit for that to come up here, but let me just start to describe it.  
It is a I'm gonna say a robust area within Axiom to be able to pull data in my opinion and what I shared with many people is that.  
I caution people using.  
Using this and trying to modify it a bit because most people who are using it have no idea of the database structure or the fields below it. So for example, here's the info manager.  
There's a number of different reports that are up here and what I have seen over time is that people come in and generate a report and create a couple different conditions. We get to a meeting and I've got four people who said I just pulled this data from Axiom and they all have different results.  
That we have not found a way to.  
People to understand how to use this, us to give them direction to use that. All of these first tabs are reports that have been developed by Exan.  
Um. And then the last one is these custom reports. These are reports that we would create within Crystal Reports. Um, you know. So when you run the report, it will um.  
I'm up with the end.  
That.  
It opens up within a crystal report here. I can I can see the data and and work from that point. I can export it as a PDF and do some other things. I'm going to get into more detail much later on on the info manager, but I just wanted to at least show real generally that within Axiom.  
Under the info manager there are some canned reports and then there are some custom reports.  
There is. I'm living at that point.  
We minimize this and come back.  
So another tool that can be used is Crystal Reports and I I sent a message to Cash and Kaden that you should reach out to ITS and get the 20 the 2008 version of Crystal Reports installed.  
The reason that we're doing the 2008 is that that's the one that's available through the university. Also, and even just a few years ago, we were asking Exan what was because we couldn't use the most recent version. We tried it at one time and found out it wasn't compatible.  
I know that at this point they have the 2013 version of Crystal Reports as the.  
The runtime version of the Crystal Reports. So I'm assuming we might be able to go up to version 13 of Crystal Reports, but the reason we stayed at 8 is that it's readily available through the university. That would be something worth looking at if we wanted to, but my comment would just be careful. Don't.  
Upgrade to the most recent version because it isn't compatible. It may not be completely compatible with XM. The reason the crystal reports are there is because they are integrated within Axiom. So if you remember when I showed you the reports here.  
Um, each of these reports.  
These reports are created in Crystal Reports and we would have the ability to create new reports or edit these reports in the in this tab of the custom reports area. The Crystal Reports is also used in a few other places within Axiom. We'll probably get to those at some point.  
But again, the purpose that I wanted to show was these are the tools. So Info Manager is a tool, Crystal Reports is a tool to pull data and we would need that because through Crystal Reports I can connect directly to the Oracle database.  
And if I wanted to use a table other than those 30 that are available in the data staging area, I would need to use Crystal Reports or another tool, but Crystal Reports is one of them.  
Since we now have that staging database, we can use Microsoft.  
Server. Bring that one up.  
And the important thing to remember in this is that what we're looking at here is. So I'm going to go into the staging database.  
When I go out, the table that we have access to here is this staging.  
And here's the 30 tables that are available to us. The thing to remember is that when we're pulling data today, we need to recognize that this is data through the end of yesterday and the ITS pulls it overnight.  
The process starts and it's running for several hours. I don't remember if it starts at 10:00 at night, running till one or two in the morning. It does take several hours to go through. So in in essence since our day.  
Typically ends at 5:00. Whatever is in through 5:00 will be there, but it really is anything up to the time of that data poll. So if someone really came in later in the day and entered something, but if they came in early this morning and entered it, it's not going to appear.  
It's also possible since we are using like the musad server does pull data from.  
The different from the different databases. So we we mostly pull data from the MUSAT server from the MSSQL server. The reason for that is to take a hit off of the production database. There were many years here where.  
The the live version of Axiom was overworked. People in the clinics were getting 20 to 32nd delays for actions to happen, so we.  
Chose to completely separate those data requests from the.  
Requirements server or from the dashboard, they're going to call out to this staging server. They're not going to call out to the live database. So whenever possible we should continue to do that, pull pull the data from this.

<img src="media/xkgo9wdp0epobdocuodmx.png" style="width:0.30208in;height:0.30208in" />**  
Keyes, Tom** 28:31  
Mm.

<img src="media/zumr19efqzuwwbkaaeuwo.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 28:39  
And recognizing that there is about a, there is the one day delay, it's deleted information, but that is true of the dashboard is that that dashboard is a one day old data.  
And then?  
So we're talking about extracting it from Python. So within Django or even just from the desktop, we can use the connection information to go out there. So that's a another tool to get to these databases.  
I recently came across that within the PC here.  
That there's also a tool.  
Um, so if I type SQL plus.  
It will look for me to connect here. I type in the connection username. I won't go through it now and the user and it will connect me in. I'm I'm in an SQL environment for Oracle.  
So now I can load scripts and run them from here. So this is another good method for us to be able to access the Oracle databases and again I'd be able to access either the production one development one.  
Or the training one.  
And then the last thing I wanted to cover under the apps is not a tool, but kind of where the source files are.  
I'm gonna start back in at the at the Informatics directory if I go to administration.  
Crystal reports.  
And again, Crystal reports, because there was a time that university was using some other reports here, but go to Crystal reports here. Within this area now are a number of either Crystal reports or SQLS that we've developed to answer questions and do queries.  
I'd say over the last 10-12 years.  
For example, if you come into clinical sciences, often by date, sometimes indicating who is asking it what the request was.  
But there's just a number of items out here indicating what was the SQL that was used to generate it. Here's the data that was generated. This is helpful because some of these requests will come up again and again, so I can go back to the survey from last year.  
Copy it over now for the next year, 2022, and then just modify, you know, review those SQLS, see what I need to modify to work from there. The important thing to to note is that this is where you're going to find either the crystal reports or the SQLS.  
Um for the data?  
Then the last thing that I wanted to show about these apps and source files is within Axiom if the report is one of these custom reports that we do.  
It's possible to go in and get that. So let's say this this report that I had run in here.  
When I get to the report, if I come up to this extraction area.  
I can say give me the give me that crystal report.  
Name it whatever you want and where you're going to pull it, and that will bring a local copy down to you. When you export, there's a lot of different things that you're going to export. If you changes the PDF, you're going to get the PDF of the report. But this is helpful to know that if you need the report and you can't find it, you can get the report downloaded locally.  
Get there.  
You're gonna see later on we're gonna go through how when we're working with the info manager of how to post reports and I'll show you where where you can do that in the background, but but I wanted to let you see kind of in this area.  
That idea that if you're looking for the source file for a crystal report that's within Axiom, you can look in the crystal reports area, but you may also find it here. So when I came there were already, I don't know 3040 reports that were created by ITS and or.  
Exam as the school had been using it for a few years and I don't know where the source files were retained on those. I don't have access to that, but if I needed to, I can always extract the report, open it up in crystal report and then upload it again into something.  
Back into X, but that's how you can get.  
Um.  
That's what I was gonna cover on apps. Any questions on that? Those those are kind of the tools to access them.  
OK, so I'm going to start talking about the people within Axiom, and I don't know if I'm going to finish this today, but let me start with it. So the first thing I want to talk about is let's open up Axiom and take a look at a few things.  
I'm just gonna move this over to another window here and then I will have Axiom open.  
Some of these things you may know already, but I think it's helpful within Axiom. The way to get to, I'm going to say that all of these are related to patients now is we'll start with the Rolodex and this is.  
It used to be called Rolodex, and that's why I'm calling it that way here. They're just calling it patients at this point.  
From this point here on the right side, it's possible for people to have a list of patients that they use regularly and these check marks are saying always bring this one up. So there's a couple test patients out there and this would be a quick way for me to access them.  
Otherwise I would type in a name or chart number. So let's let's just try this. I'm going to pull up on my record. So I'm I'm going to start with the last name, a comma, first name.  
And that would bring up a record that I have here.  
Let me just do.  
Years ago, one of the people created a number of test cases for Homer Simpson and Marge Simpson and and some others. So the the challenge now I'll get to that later, but.  
You'll see that there's a lot of charts out here for Homer if.  
The thing I wanted to point out was in this list, when you click on it, when the name appears down here, that's telling you the patient that you have selected. If that's blank, you don't have a patient selected and if you try to do something.  
It it may come up with no information because you don't have a patient selected. So you want to be careful to make sure you have a patient selected. Now when I have the patient selected and I go out to another area, that's when I'll that's the patient that they'll use to pull that information.  
So this is something that comes up often with.  
Students when they're first using it and faculty and staff is there, they get confused about.  
Not seeing the correct data. This is the important part is make sure that they're selected down.  
I'm gonna close this again and show you how to get there once you have a patient selected.  
You can click on their patient card and there is a lot of information here about this particular patient. If you come up into this Gray area up here and you click left click once, you're going to open up another window which is more information about the patient.  
Uh.  
Most of the information in these tabs is in the patient record, and we'll get to that in, you know, in a while there, but this is information.  
Personal information codes is used and I was mentioning to Tom Kees just the other day that Axiom has very little ability for us to configure our unique.  
Fields. They give us 5 alert fields, 5 office code fields, and then there's another place in here. They give us five more fields in another spot from what I remember.  
And so this is where we can configure some things, but we're very limited. Oh, these here, these custom fields, there's five more here that got defined, but we've already defined them all. So we have very limited space when we have something new we want to track. It's hard for us to put that here.  
But this is where all of these things are stored in the patient record. There's clinical information about the patient. These next three, the guarantor, the employer and the insurance are.  
Additional tables.  
Beside the patient table that contain information, but these other ones are primarily for the most part fields that exist within the patient table. I wanted to show you how to get to that here.  
And on here I've listed patient info, but I think what I'm really talking about was this is the patient info that was on the.  
Reaching the card.  
One other thing I want to point out that we implemented several years ago is the use of student charts. So what was happening prior to probably 20/20/19 or so?  
Is when a new class of students came in, they would send the students over to our registration area and every student was entered into the database as a patient.  
And then that's where the student could track service points and some other things that they do in Axiom. But the challenge and problem that came up was that some of the students who come to us are from the Wisconsin area.  
And they were already coming to the school as a patient for maybe orthodontics or something else. So their record already existed and now their student record that existed here was really their student record and their patient record.  
And the thing that complicated it more was in their first year or two, they often work on each other to as some test things and training things. So then they would give access to the other students to work on them.  
And so now we were exposing a student's actual patient chart to another student because they're doing a training exercise.  
So what we did then was separate out and created what they call now is more of the.  
Uh, what we call the student chart. I'm gonna try this.  
And what we did in that case then was assign the chart number to be the student's provider.  
So, so Alexander Hernandez is really his provider code is S 3443. So this chart now is the chart for the student information. It's also stored in a little configured in a little different way, so it's not considered a.  
It's not treated the same way patient charts are. And then the instruction to the students is if Alexander wanted to have treatment here, Alexander needs to get a patient chart created.  
With the name Alexander Hernandez, and then he'll have a different um.  
Chart number. So technically there'll be two Alexander Hernandez, one which is this S chart, which is the student chart and then the other chart which will be his patient one and the patient one would not be accessible to the other students and that's the way that's protected.  
So, so that's helpful to know at least that distinction. There are a few more scenarios like that where we have different types of patient records that aren't accessible everywhere, but I don't plan to go into that right now.  
Questions on any of that?  
OK.  
Then let's go to the database and take a look at the patient record.  
And I'm gonna go to that.  
Add a dictionary again for this.  
I'm going to find the patient table.  
This patient number is  
Used.  
Throughout many tables within Axiom. So Axiom has been application since the late 1990s. I think the school moved to it in about 2002.  
So it had already existed three or four years prior to that, but it has grown.  
And combine different things. And the reason I mentioned it is that this patient ID exists for many tables and unfortunately within Axiom there are other sets and other areas that use something that they called patient 2.  
A patient really has two numbers. The second number doesn't exist here. You have to go to another table to find that patient number, patient two number for this patient. Don't know the background from it or why that exists in Axiom.  
But I just want to point out that there are some things and notes is the the big one that exists.  
The notes that are recorded in Axiom are based on a patient two number, so you always have to translate to find the actual patient by going to the patient two table, finding the patient number, and then you can get back to this table.  
So it's a little convoluted and and I'll show you with an axiom as we go through these is the way they name them is not consistent across the tables. For many of them the patient one is pointing to this patient primary key.  
I'm not going to go through every field here, I'm just going to kind of go through real generally. You'll get a sense of what is here, but for the most part, the static information about the patient does exist here.  
The name, address, phone numbers, the status. I'm gonna go through status in a little bit. What it's talking about is what is the status?  
Of this patient and and I'll tell you in general it should be the patient is active, should just recall state the patient is inactive.  
The sex is here and they added these.  
Recently because the oh, there were only three about two years ago, so this got added marital status.  
Here are.  
Ten of those special coding that can't exist. We saw that before the office ones in the alerts.  
Axiom does keep track of some dates, but you're gonna see that.  
One that I try to use, which being the last visit, does not necessarily mean their last appointment. It is the last time a select number of things happened and sometimes it could be a note that was entered, it could be.  
So you want to be careful that this is the description that's given to us, but you you don't want to assume that that you know exactly what that means. You're gonna you're gonna want to test that a bit before we use it to know what is Axion mean by first treatment.  
There's not documentation anywhere to tell you exactly what that means.  
Just trying to look to see this. Here are more of those custom codes that can exist. We saw all of those in the patient card.  
This is contact information.  
Again, these information down here, X-ray C, date X-ray received, all of those are things to track the last time something was happening.  
More custom text.  
That is it on the patient one, a number of records in there. The chart does exist in here. Unfortunately with this you don't have a way to sort it so that they're in alphabetical order. So when you're looking for the chart you have.  
To kind of remember where is it to be this search for it, but here's the chart and that we'll we'll use quite a bit.  
There is a concept that I wanted to talk about about patients and that's the way that people are going to ask when they're looking for data.  
They may want to say I want to know how many patients were seen in the clinic this week and we need to follow up when when they ask that because it could mean.  
Commonly two different things. What's the total number of patients that we're seeing and more of like what were the total number of visits for that for any patient. So the same patient might be here five times, they're going to count as 5.  
So the the term that is often used to help distinguish it would be are they looking for unique patients? Are they looking for unduplicated patients for that run? So in other words, this week.  
How many unduplicated? How many unique patients did we have, or how many total patients did we have? Same person might come counted multiple times. So that's an important one that you want to be sure that you understand what they're asking for.  
Because it's it may be in their mind, but they aren't thinking of this couple different ways it gets pulled. But every almost everyone that you're gonna want to do, you need to try to clarify that.  
Distinct, unique, unduplicated or the total ones.  
Um.  
Let me talk. Tell you what, while we're on patients, I'm going to skip down to this section because I think this is helped. I want to talk about some known conflicts and issues that exist with the patient table. So one is race and ethnicity.  
Within our database.  
Typically we only are recording race and ethnicity or 40% or fewer of our patients. The information exists on the health history form.  
But if the patient hasn't filled it out, it does not get entered in and.  
There is not a procedure or a policy for us to.  
Query further with the patient to get that information. So quite often it is not there. The reason that's important is that many of the research projects wanted that information and it isn't there. So so that's one of the qualifications that I often tell people.  
Is when they're pulling this, they're gonna get a lot of null data because it's, you know, it is not always recorded for the patient quite often.  
Another challenge with race and ethnicity is that it is recorded in several different places in the in the chart here.  
I'll tell you.  
I'm gonna bring up large.  
So I'm going into the patient card again and.  
One place that it is, it exists in the database, but we typically don't put it there.  
They moved this recently, so I'm just looking for it here.

<img src="media/urgvmfxjpozo9vg1qqyor.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 51:25  
Go back. There was a button there on the personal right in the center column for racism and the right there above your person.

<img src="media/b715r9qkpb4ffohk8njdd.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 51:31  
Oh Yep, yes, yes. So this is the one that is not used much. I'm not going to select it here, but they could select the race and they could select the ethnicity, but they typically don't use this one.  
But it's a place that exists and then we have to look for this one as well. The other place would be in the codes. We do have one called ethnicity here, but it's not. I don't think that this is the true breakdown of.  
Ethnicity. It may mix race and ethnicity in here, but this would be the common place to look for it would be under this tab. So this is 1 area which is ethnicity and then there's two areas here. One is a table called race.  
Where this exists and another is called ethnicity, where this exists. There's three different places in Axiom where that data is stored. So I point that out. It mostly happens when we're dealing with research issues, but it's just important to know that's that's one of the challenges that exists here.  
This is Smith in ethnicity.  
This other one is there has been a use across many years now to change the chart number for different purposes.  
Show you what I mean here. Um.  
So we have a number of charts that begin with P and they put the letter P in the front of a chart number to indicate that this is a pediatric patient.  
The problem that happens is that if the patient when they get and I forget if it's when they're 16 or 15 at some point when they become an adult and can move to the other clinic.  
At least sometimes, I don't know if it's all of the times they take the P out of the chart number. What's confusing then is now when you go search for different things, but patient ID at least stayed the same. But if someone had a reference to that chart number, it doesn't exist and you can't find it.  
You'd have to know and guess that you would search for the chart number without the P, and I'll tell you, most people aren't aren't aware of that. So that's one instance of how people have changed the chart number for a condition. Another one that happened is ortho.  
It also used that scenario where if the person was coming in and starting as a patient for the ortho clinic, so they're not necessarily coming to the predoc, they'll put it on at the beginning.  
There was a time, let me just see if any are here. And what they started to do was there was a faculty here whose last name began with B and he was doing a research study. So they decided that if this chart was going to be used for that faculty's research, they're going to have a.  
B in here. So then they knew when they checked in if that person was part of the study. Well again, the challenge was what if now you started searching for O679119? You wouldn't find it because they added AB in there.  
But but that that was kind of the most egregious one. We took patients that have been here for several years just to add in a letter to them and now you I I don't know how you'd find them.  
So, so that does exist that we change the letters of some of them. Tell you what, while we're on it, let me just show you a couple others that exist.  
I put AC out there. We used to have two external clinics. This one was Coggs COGGS and then I think the other was and J is the other one.  
And this was the Johnson clinic. Now some of these patients beginning with C, beginning with J are being seen here. I don't know that if they started to remove any of those C's or J's or if they left them there, but they they.

<img src="media/bfwk_883jnzabypi6qo02.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 55:46  
The.

<img src="media/z34tz3ie60-v1jo65pqjd.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 56:00  
Kind of mixing the chart number to be to record two or three conditions rather than to just be a chart number.

<img src="media/ibvp79omcmbhk9zubxztv.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 56:09  
I might have missed this, but they don't do that anymore, correct?

<img src="media/c_bgidbgjeouqewqzj4bd.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 56:12  
Well, Cogs and Johnson don't exist anymore, so no no new ones are being created. But I think that you would see that there are some current patients that still have those letter distinctions there.  
Another known conflict or issue is the blended use of the status field.  
So this patient is listed in the screening area and and to me I think that would be another valid one. So when I click on this status, you're gonna see a ton of responses here. All of these are active status.  
And then sometimes they have an extra letter to distinguish something else about them. Endo, the emergency only, grand process only. But it so when I'm going to go search for an active patient.  
I'm gonna start with if the 1st letter is a, it's active. What's happened in some of these reports is that we just use the search for active and then they started adding these extra ones in. My search for active now is missing these.  
Because they got added in and no one went back to update the reports because of that. So in my view, we need to clean up the status field so that it's active or it's inactive or it's recalled.  
And they have a couple of different conditions of recall, but but again the I think the status is one of those three and we should be using another field to keep track of some of these other conditions, but it's an important one to know because it it.  
This comes up when they people are doing searching. Another issue with this is that.  
There is not a good discipline here at the school that we're all entering this consistently and this came up recently in one of the clinics. They wanted to do some research and they told us pull the status field of this. In this case it was endo.  
And they thought it meant a certain condition, and it was the opposite of what it was. And so they didn't even know what their status meant. They were pulling up charts for things that was the opposite condition of what they were really looking for.  
So, so even though these are existing and are created because the clinics are asking for that, they do not have a good discipline to know what that means and that they're all applying it consistently. So, so unfortunately to say this status flag.  
Exists, but it is not accurate.  
Um.

<img src="media/jtgdia1royyt_e_lzqz-w.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 59:02  
I just, I don't mean interrupt, but I have a hard stop at 11. I'm having to back out now.

<img src="media/f_p6j6cmncbqjlmdigxq2.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 59:05  
Yeah, tell you what, let.  
Yeah, let's, let's. I'm gonna stop here and then I'll pick up with this when we meet again. All right. All right. Thank you. So, Stacy, let's go ahead and you can turn off the recording and then we'll schedule another time to continue from here.

<img src="media/0bsuako0rhlvq3zh3ubcy.png" style="width:0.30208in;height:0.30208in" />**  
Myers, Cashius** 59:13  
All right, sounds good.

<img src="media/vrumsfo_4u6g807ba1zcr.png" style="width:0.30208in;height:0.30208in" />**  
Enters, Kaden** 59:13  
OK.

<img src="media/fmzlhesi0hgk0okamachr.png" style="width:0.30208in;height:0.30208in" />**  
Keller, Stacy** 59:22  
Oh, OK.

<img src="media/votnkiekbn7mim-xp78tb.png" style="width:0.30208in;height:0.30208in" />**  
Wirtz, Thomas** 59:24  
Thank you.

<img src="media/9wjhrhrt3ut0tx96cljaq.png" style="width:0.30208in;height:0.30208in" />**  
Keller, Stacy** 59:25  
Sure.

<img src="media/mxhrcfytebcs9xxgupsg0.png" style="width:0.22917in;height:0.22917in" />**  
Keller, Stacy** stopped transcription
