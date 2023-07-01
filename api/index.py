from flask import Flask

import json
import openai
import pandas as pd
import random

df_batter = pd.read_csv('IPL2023_Batsman_clean.csv')
df_bowler = pd.read_csv('IPL2023_Bowler_clean.csv')
df_scoreboard = pd.read_csv('IPL2023_Match_Scoreboard_clean.csv')
df_matches = pd.read_csv('IPL2023_Matches_clean.csv')

app = Flask(__name__)

batsman = ['Devon Conway', 'Ruturaj Gaikwad', 'Moeen Ali', 'Ben Stokes', 'Ambati Rayudu',
           'Shivam Dube', 'Ravindra Jadeja', 'MS Dhoni', 'Mitchell Santner',
           'Wriddhiman Saha', 'Shubman Gill', 'Sai Sudharsan', 'Hardik Pandya',
           'Vijay Shankar', 'Rahul Tewatia', 'Rashid Khan', 'Prabhsimran Singh',
           'Shikhar Dhawan', 'Bhanuka Rajapaksa', 'Jitesh Sharma', 'Sikandar Raza',
           'Sam Curran', 'Shahrukh Khan', 'Mandeep Singh', 'Rahmanullah Gurbaz',
           'Anukul Roy', 'Venkatesh Iyer', 'Nitish Rana', 'Rinku Singh', 'Andre Russell',
           'Shardul Thakur', 'Sunil Narine', 'KL Rahul', 'Kyle Mayers', 'Deepak Hooda',
           'Krunal Pandya', 'Marcus Stoinis', 'Nicholas Pooran', 'Ayush Badoni',
           'Krishnappa Gowtham', 'Prithvi Shaw', 'David Warner', 'Mitchell Marsh',
           'Sarfaraz Khan', 'Rilee Rossouw', 'Rovman Powell', 'Aman Hakim Khan',
           'Axar Patel', 'Kuldeep Yadav', 'Chetan Sakariya', 'Mukesh Kumar',
           'Yashasvi Jaiswal', 'Jos Buttler', 'Sanju Samson', 'Devdutt Padikkal',
           'Riyan Parag', 'Shimron Hetmyer', 'Ravichandran Ashwin', 'Abhishek Sharma',
           'Mayank Agarwal', 'Rahul Tripathi', 'Harry Brook', 'Washington Sundar',
           'Glenn Phillips', 'Abdul Samad', 'Adil Rashid', 'Bhuvneshwar Kumar',
           'Umran Malik', 'Rohit Sharma', 'Ishan Kishan', 'Cameron Green',
           'Suryakumar Yadav', 'Tilak Varma', 'Nehal Wadhera', 'Tim David',
           'Hrithik Shokeen', 'Arshad Khan', 'Virat Kohli', 'Faf du Plessis',
           'Dinesh Karthik', 'Glenn Maxwell', 'Mark Wood', 'Abishek Porel',
           'Anrich Nortje', 'David Miller', 'Dhruv Jurel', 'Jason Holder', 'Umesh Yadav',
           'Michael Bracewell', 'Harshal Patel', 'Shahbaz Ahmed', 'Anuj Rawat',
           'David Willey', 'Karn Sharma', 'Akash Deep', 'Anmolpreet Singh',
           'Aiden Markram', 'Romario Shepherd', 'Manish Pandey', 'Lalit Yadav',
           'Tristan Stubbs', 'Piyush Chawla', 'Ajinkya Rahane', 'Abhinav Manohar',
           'N Jagadeesan', 'Matthew Short', 'Harpreet Brar', 'Rahul Chahar',
           'Nathan Ellis', 'Mohit Rathee', 'Jaydev Unadkat', 'Ravi Bishnoi',
           'Avesh Khan', 'Yash Dhull', 'Mustafizur Rahman', 'Adam Zampa', 'Rishi Dhawan',
           'Heinrich Klaasen', 'Mahipal Lomror', 'Yudhvir Singh', 'Atharva Taide',
           'Harpreet Singh Bhatia', 'Kagiso Rabada', 'Alzarri Joseph', 'Trent Boult',
           'Suyash Prabhudessai', 'Wayne Parnell', 'Wanindu Hasaranga', 'Marco Jansen',
           'Mayank Markande', 'Liam Livingstone', 'Arshdeep Singh', 'Jason Roy',
           'Litton Das', 'Varun Chakaravarthy', 'Philip Salt', 'Prerak Mankad',
           'Harpreet Singh', 'Jofra Archer', 'Vijaykumar Vyshak', 'Mohammed Siraj',
           'Abdul Basith', 'David Wiese', 'Ripal Patel', 'Ishant Sharma',
           'Arjun Tendulkar', 'Jason Behrendorff', 'Riley Meredith', 'Priyam Garg',
           'Akeal Hosein', 'Josh Hazlewood', 'Amit Mishra', 'Naveen-ul-Haq',
           'Manan Vohra', 'Karan Sharma', 'Harshit Rana', 'Vaibhav Arora',
           'Sandeep Sharma', 'Quinton de Kock', 'Swapnil Singh', 'Kedar Jadhav',
           'Deepak Chahar', 'Tushar Deshpande', 'Vishnu Vinod', 'Noor Ahmad',
           'Praveen Dubey', 'Joe Root', 'KM Asif', 'Dasun Shanaka', 'Mohammed Shami',
           'Mohit Sharma', 'Sanvir Singh', 'Fazalhaq Farooqi', 'Vivrant Sharma']

out_by = ['Mohammed Shami', 'Alzarri Joseph', 'Rashid Khan', 'Joshua Little', 'Not Out', 'Rajvardhan Hangargekar',
          'Tushar Deshpande', 'Ravindra Jadeja', 'Tim Southee', 'Varun Chakaravarthy', 'Umesh Yadav', 'Sunil Narine',
          'Arshdeep Singh', 'Nathan Ellis', 'Sikandar Raza', 'Rahul Chahar', 'Sam Curran', 'Chetan Sakariya',
          'Axar Patel', 'Kuldeep Yadav', 'Khaleel Ahmed', 'Mark Wood', 'Avesh Khan', 'Fazalhaq Farooqi', 'T Natarajan',
          'Umran Malik', 'Trent Boult', 'Yuzvendra Chahal', 'Jason Holder', 'Ravichandran Ashwin', 'Akash Deep',
          'Mohammed Siraj', 'Reece Topley', 'Michael Bracewell', 'Karn Sharma', 'Harshal Patel', 'Arshad Khan',
          'Cameron Green', 'Ravi Bishnoi', 'Moeen Ali', 'Mitchell Santner', 'Anrich Nortje', 'Mitchell Marsh',
          'retd hurt(Not Out)', 'Run Out', 'David Willey', 'Shardul Thakur', 'Suyash Sharma', 'Krunal Pandya',
          'Yash Thakur', 'Amit Mishra', 'Adil Rashid', 'Bhuvneshwar Kumar', 'Mukesh Kumar', 'Rovman Powell',
          'Sandeep Sharma', 'Sisanda Magala', 'Jason Behrendorff', 'Piyush Chawla', 'Kumar Kartikeya', 'Marco Jansen',
          'Mayank Markande', 'Wayne Parnell', 'Mustafizur Rahman', 'Hrithik Shokeen', 'Riley Meredith', 'Akash Singh',
          'Adam Zampa', 'Mohit Sharma', 'Kagiso Rabada', 'Harpreet Brar', 'Andre Russell', 'Lalit Yadav',
          'Vijaykumar Vyshak', 'Wanindu Hasaranga', 'Yudhvir Singh', 'Krishnappa Gowtham', 'Duan Jansen',
          'Lockie Ferguson', 'Hardik Pandya', 'Noor Ahmad', 'Glenn Maxwell', 'Maheesh Theekshana',
          'Matheesha Pathirana', 'Arjun Tendulkar', 'Marcus Stoinis', 'Ishant Sharma', 'Nitish Rana', 'Anukul Roy',
          'Naveen-ul-Haq', 'Jofra Archer', 'Liam Livingstone', 'Kulwant Khejroliya', 'Washington Sundar',
          'Kuldip Yadav', 'Harshit Rana', 'Akeal Hosein', 'Abhishek Sharma', 'Josh Hazlewood', 'Rishi Dhawan',
          'Kartik Tyagi', 'Aiden Markram', 'Vaibhav Arora', 'Deepak Chahar', 'Akash Madhwal', 'Tristan Stubbs',
          'Mohsin Khan', 'Chris Jordan', 'KM Asif', 'Glenn Phillips', 'Praveen Dubey', 'Yash Dayal', 'Retd Hurt',
          'Shahbaz Ahmed', 'Navdeep Saini', 'Mayank Dagar']

bowler = ['Mohammed Shami', 'Hardik Pandya', 'Joshua Little', 'Rashid Khan', 'Alzarri Joseph', 'Yash Dayal',
          'Deepak Chahar', 'Tushar Deshpande', 'Rajvardhan Hangargekar', 'Mitchell Santner', 'Ravindra Jadeja',
          'Umesh Yadav', 'Tim Southee', 'Sunil Narine', 'Varun Chakaravarthy', 'Shardul Thakur', 'Sam Curran',
          'Arshdeep Singh', 'Nathan Ellis', 'Sikandar Raza', 'Rishi Dhawan', 'Rahul Chahar', 'Harpreet Brar',
          'Kyle Mayers', 'Jaydev Unadkat', 'Krishnappa Gowtham', 'Avesh Khan', 'Mark Wood', 'Ravi Bishnoi',
          'Khaleel Ahmed', 'Mukesh Kumar', 'Chetan Sakariya', 'Axar Patel', 'Kuldeep Yadav', 'Bhuvneshwar Kumar',
          'Fazalhaq Farooqi', 'Washington Sundar', 'T Natarajan', 'Adil Rashid', 'Umran Malik', 'Trent Boult',
          'KM Asif', 'Jason Holder', 'Ravichandran Ashwin', 'Yuzvendra Chahal', 'Navdeep Saini', 'Mohammed Siraj',
          'Reece Topley', 'Akash Deep', 'Harshal Patel', 'Karn Sharma', 'Michael Bracewell', 'Glenn Maxwell',
          'Jason Behrendorff', 'Arshad Khan', 'Jofra Archer', 'Piyush Chawla', 'Cameron Green', 'Hrithik Shokeen',
          'Krunal Pandya', 'Yash Thakur', 'Ben Stokes', 'Moeen Ali', 'RS Hangargekar', 'Anrich Nortje',
          'Mitchell Marsh', 'David Willey', 'Shahbaz Ahmed', 'Suyash Sharma', 'Deepak Hooda', 'Amit Mishra',
          'Aiden Markram', 'Rovman Powell', 'Sandeep Sharma', 'Murugan Ashwin', 'Sisanda Magala', 'Dwaine Pretorius',
          'Kumar Kartikeya', 'Lockie Ferguson', 'Marco Jansen', 'Mayank Markande', 'Mohit Rathee', 'Wayne Parnell',
          'Riley Meredith', 'Tilak Varma', 'Mustafizur Rahman', 'Lalit Yadav', 'Akash Singh', 'Maheesh Theekshana',
          'Kuldeep Sen', 'Adam Zampa', 'Mohit Sharma', 'Kagiso Rabada', 'Matthew Short', 'Andre Russell',
          'Vijaykumar Vyshak', 'Wanindu Hasaranga', 'Yudhvir Singh Charak', 'Arjun Tendulkar', 'Duan Jansen',
          'Noor Ahmad', 'Matheesha Pathirana', 'Naveen-ul-Haq', 'Liam Livingstone', 'Ishant Sharma',
          'Kulwant Khejroliya', 'Anukul Roy', 'Nitish Rana', 'Mayank Dagar', 'Marcus Stoinis', 'Jayant Yadav',
          'Rahul Tewatia', 'David Wiese', 'Vaibhav Arora', 'Kuldip Yadav', 'Gurnoor Brar', 'Ayush Badoni',
          'Harshit Rana', 'Akeal Hosein', 'Abhishek Sharma', 'Josh Hazlewood', 'Mahipal Lomror', 'Akash Madhwal',
          'Kartik Tyagi', 'Raghav Goyal', 'Tristan Stubbs', 'Mohsin Khan', 'Swapnil Singh', 'Vivrant Sharma',
          'Obed McCoy', 'Chris Jordan', 'Joe Root', 'Yudhvir Singh', 'Glenn Phillips', 'Praveen Dubey', 'Nitish Reddy',
          'Himanshu Sharma']

team = ['Gujarat Titans', 'Chennai Super Kings', 'Kolkata Knight Riders', 'Punjab Kings', 'Lucknow Super Giants',
        'Delhi Capitals', 'Sunrisers Hyderabad', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Mumbai Indians',
        'Sunrisers Hyderabad']

city = ['Ahmedabad', 'Mohali', 'Lucknow', 'Hyderabad', 'Bengaluru', 'Chennai', 'Delhi', 'Guwahati', 'Kolkata',
        'Lucknow', 'Mumbai', 'Jaipur', 'Dharamsala']


def pick_random_items(lst):
    if lst == 'batsman':
        return random.sample(batsman, 3)
    elif lst == 'bowler':
        return random.sample(bowler, 3)
    elif lst == 'team':
        return random.sample(team, 3)
    elif lst == 'city':
        return random.sample(city, 3)
    elif lst == 'out_by':
        return random.sample(out_by, 3)
    return random.sample(lst, 3)


def get_query_answer(query):
    result = eval(query)
    print("Answer: ", result)
    return result


def retry_on_failure(query, max_retries=1, delay=5):
    for i in range(max_retries):
        try:
            # Attempt to call the function
            answer = get_query_answer(query)
            if (pd.isnull(answer)):
                request_new_q(query, "No answer found in table")
            else:
                return answer
        except Exception as e:
            print(query)
            print(e)
            request_new_q(query, str(e))
    print(f"Failed to execute function after {max_retries} attempts.")


def request_new_q(query, reason):
    prompt_message = "Please generate a new query. I am unable to use current query because " + reason
    print(prompt_message)
    return None


def generate_question(question_prompt, pandas_query, answer_type):
    answer = retry_on_failure(pandas_query)
    options = pick_random_items(answer_type)
    if answer in options:
        options.remove(answer)
    options.append(answer)
    random.shuffle(options)
    return {"question": question_prompt, "options": options, "answer": answer}


def generate_question_query():
    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "user",
                 "content": "these are 4 datasets that I have related to IPL 2023. I want to ask fun trivia questions to a user basis this dataset - try a random question every time. \n\nGenerate the question in function format as requested\n\n\\n\\nIPL2023_Batter.csv named as df_batter\\nmatch_no - No of match according to IPL schedule\\nBatsman - Name of the Batsman in that particular match\\nteam - Batsman played in which team\\nRun - Run scored by that Batsman\\nBall- The number of balls he took to score the runs\\n4s - How much 4 he scored in that match\\n6s - How much 6 he scored in that match\\nout_by - name of bowler who outed him\\n\\n\\nIPL2023_Bowler.csv named as df_bowler\\nmatch_no - No of match according to IPL schedule\\nBowler - Name of the Bowler in that particular match\\nteam - Bowler played in which team\\nover_ - How much over he did in that match\\nrun- How much runs he gave in that match\\nwicket - How much wicket taken by that bowler\\nNo_ball - How much No ball he done\\nECO - economy rate is the average number of runs\\n\\n\\nIPL2023_Match_Scoreboard.csv named as df_scoreboard\\nmatch_no - No of match according to IPL schedule\\nHome_team_run - Total Runs done by home team\\nHome_team_wickets - Home team's total wickets gone\\nHome_team_over - Total overs played by Home team\\nAway_team_run - Total Runs done by Away team\\nAway_team_wickets - Away team's total wickets gone\\nAway_team_over - Total overs played by Away team\\n\\n\\nIPL2023_Matches.csv named as df_matches\\nmatch_no - Match number according to IPL schedule\\ncity - Location of match\\ndate_of_match - Date of Match\\nvenue - Venue of the match\\nHome_team - Team playing in home ground\\nAway_team - Team not playing in home ground\\ntoss_winner - Team that won the toss\\nwinner - Team that won the match\\nman_of_the_match - Player awarded \\\"Man of the Match\\\"\\nresult - Game won by 1st batting team or 1st bowling team\\nresult_margin - \\neliminator\\numpire1\\numpire2\n\n\nHere are some data Batsmen:  ['Devon Conway' 'Ruturaj Gaikwad' 'Moeen Ali' 'Ben Stokes' 'Ambati Rayudu'\n 'Shivam Dube' 'Ravindra Jadeja' 'MS Dhoni' 'Mitchell Santner'\n 'Wriddhiman Saha' 'Shubman Gill' 'Sai Sudharsan' 'Hardik Pandya'\n 'Vijay Shankar' 'Rahul Tewatia' 'Rashid Khan' 'Prabhsimran Singh'\n 'Shikhar Dhawan' 'Bhanuka Rajapaksa' 'Jitesh Sharma' 'Sikandar Raza'\n 'Sam Curran' 'Shahrukh Khan' 'Mandeep Singh' 'Rahmanullah Gurbaz'\n 'Anukul Roy' 'Venkatesh Iyer' 'Nitish Rana' 'Rinku Singh' 'Andre Russell'\n 'Shardul Thakur' 'Sunil Narine' 'KL Rahul' 'Kyle Mayers' 'Deepak Hooda'\n 'Krunal Pandya' 'Marcus Stoinis' 'Nicholas Pooran' 'Ayush Badoni'\n 'Krishnappa Gowtham' 'Prithvi Shaw' 'David Warner' 'Mitchell Marsh'\n 'Sarfaraz Khan' 'Rilee Rossouw' 'Rovman Powell' 'Aman Hakim Khan'\n 'Axar Patel' 'Kuldeep Yadav' 'Chetan Sakariya' 'Mukesh Kumar'\n 'Yashasvi Jaiswal' 'Jos Buttler' 'Sanju Samson' 'Devdutt Padikkal'\n 'Riyan Parag' 'Shimron Hetmyer' 'Ravichandran Ashwin' 'Abhishek Sharma'\n 'Mayank Agarwal' 'Rahul Tripathi' 'Harry Brook' 'Washington Sundar'\n 'Glenn Phillips' 'Abdul Samad' 'Adil Rashid' 'Bhuvneshwar Kumar'\n 'Umran Malik' 'Rohit Sharma' 'Ishan Kishan' 'Cameron Green'\n 'Suryakumar Yadav' 'Tilak Varma' 'Nehal Wadhera' 'Tim David'\n 'Hrithik Shokeen' 'Arshad Khan' 'Virat Kohli' 'Faf du Plessis'\n 'Dinesh Karthik' 'Glenn Maxwell' 'Mark Wood' 'Abishek Porel'\n 'Anrich Nortje' 'David Miller' 'Dhruv Jurel' 'Jason Holder' 'Umesh Yadav'\n 'Michael Bracewell' 'Harshal Patel' 'Shahbaz Ahmed' 'Anuj Rawat'\n 'David Willey' 'Karn Sharma' 'Akash Deep' 'Anmolpreet Singh'\n 'Aiden Markram' 'Romario Shepherd' 'Manish Pandey' 'Lalit Yadav'\n 'Tristan Stubbs' 'Piyush Chawla' 'Ajinkya Rahane' 'Abhinav Manohar'\n 'N Jagadeesan' 'Matthew Short' 'Harpreet Brar' 'Rahul Chahar'\n 'Nathan Ellis' 'Mohit Rathee' 'Jaydev Unadkat' 'Ravi Bishnoi'\n 'Avesh Khan' 'Yash Dhull' 'Mustafizur Rahman' 'Adam Zampa' 'Rishi Dhawan'\n 'Heinrich Klaasen' 'Mahipal Lomror' 'Yudhvir Singh' 'Atharva Taide'\n 'Harpreet Singh Bhatia' 'Kagiso Rabada' 'Alzarri Joseph' 'Trent Boult'\n 'Suyash Prabhudessai' 'Wayne Parnell' 'Wanindu Hasaranga' 'Marco Jansen'\n 'Mayank Markande' 'Liam Livingstone' 'Arshdeep Singh' 'Jason Roy'\n 'Litton Das' 'Varun Chakaravarthy' 'Philip Salt' 'Prerak Mankad'\n 'Harpreet Singh' 'Jofra Archer' 'Vijaykumar Vyshak' 'Mohammed Siraj'\n 'Abdul Basith' 'David Wiese' 'Ripal Patel' 'Ishant Sharma'\n 'Arjun Tendulkar' 'Jason Behrendorff' 'Riley Meredith' 'Priyam Garg'\n 'Akeal Hosein' 'Josh Hazlewood' 'Amit Mishra' 'Naveen-ul-Haq'\n 'Manan Vohra' 'Karan Sharma' 'Harshit Rana' 'Vaibhav Arora'\n 'Sandeep Sharma' 'Quinton de Kock' 'Swapnil Singh' 'Kedar Jadhav'\n 'Deepak Chahar' 'Tushar Deshpande' 'Vishnu Vinod' 'Noor Ahmad'\n 'Praveen Dubey' 'Joe Root' 'KM Asif' 'Dasun Shanaka' 'Mohammed Shami'\n 'Mohit Sharma' 'Sanvir Singh' 'Fazalhaq Farooqi' 'Vivrant Sharma']\nOut by:  ['Mohammed Shami' 'Alzarri Joseph' 'Rashid Khan' 'Joshua Little' 'Not Out'\n 'Rajvardhan Hangargekar' 'Tushar Deshpande' 'Ravindra Jadeja'\n 'Tim Southee' 'Varun Chakaravarthy' 'Umesh Yadav' 'Sunil Narine'\n 'Arshdeep Singh' 'Nathan Ellis' 'Sikandar Raza' 'Rahul Chahar'\n 'Sam Curran' 'Chetan Sakariya' 'Axar Patel' 'Kuldeep Yadav'\n 'Khaleel Ahmed' 'Mark Wood' 'Avesh Khan' 'Fazalhaq Farooqi' 'T Natarajan'\n 'Umran Malik' 'Trent Boult' 'Yuzvendra Chahal' 'Jason Holder'\n 'Ravichandran Ashwin' 'Akash Deep' 'Mohammed Siraj' 'Reece Topley'\n 'Michael Bracewell' 'Karn Sharma' 'Harshal Patel' 'Arshad Khan'\n 'Cameron Green' 'Ravi Bishnoi' 'Moeen Ali' 'Mitchell Santner'\n 'Anrich Nortje' 'Mitchell Marsh' 'retd hurt(Not Out)' 'Run Out'\n 'David Willey' 'Shardul Thakur' 'Suyash Sharma' 'Krunal Pandya'\n 'Yash Thakur' 'Amit Mishra' 'Adil Rashid' 'Bhuvneshwar Kumar'\n 'Mukesh Kumar' 'Rovman Powell' 'Sandeep Sharma' 'Sisanda Magala'\n 'Jason Behrendorff' 'Piyush Chawla' 'Kumar Kartikeya' 'Marco Jansen'\n 'Mayank Markande' 'Wayne Parnell' 'Mustafizur Rahman' 'Hrithik Shokeen'\n 'Riley Meredith' 'Akash Singh' 'Adam Zampa' 'Mohit Sharma'\n 'Kagiso Rabada' 'Harpreet Brar' 'Andre Russell' 'Lalit Yadav'\n 'Vijaykumar Vyshak' 'Wanindu Hasaranga' 'Yudhvir Singh'\n 'Krishnappa Gowtham' 'Duan Jansen' 'Lockie Ferguson' 'Hardik Pandya'\n 'Noor Ahmad' 'Glenn Maxwell' 'Maheesh Theekshana' 'Matheesha Pathirana'\n 'Arjun Tendulkar' 'Marcus Stoinis' 'Ishant Sharma' 'Nitish Rana'\n 'Anukul Roy' 'Naveen-ul-Haq' 'Jofra Archer' 'Liam Livingstone'\n 'Kulwant Khejroliya' 'Washington Sundar' 'Kuldip Yadav' 'Harshit Rana'\n 'Akeal Hosein' 'Abhishek Sharma' 'Josh Hazlewood' 'Rishi Dhawan'\n 'Kartik Tyagi' 'Aiden Markram' 'Vaibhav Arora' 'Deepak Chahar'\n 'Akash Madhwal' 'Tristan Stubbs' 'Mohsin Khan' 'Chris Jordan' 'KM Asif'\n 'Glenn Phillips' 'Praveen Dubey' 'Yash Dayal' 'Retd Hurt' 'Shahbaz Ahmed'\n 'Navdeep Saini' 'Mayank Dagar']\nBowlers  ['Mohammed Shami' 'Hardik Pandya' 'Joshua Little' 'Rashid Khan'\n 'Alzarri Joseph' 'Yash Dayal' 'Deepak Chahar' 'Tushar Deshpande'\n 'Rajvardhan Hangargekar' 'Mitchell Santner' 'Ravindra Jadeja'\n 'Umesh Yadav' 'Tim Southee' 'Sunil Narine' 'Varun Chakaravarthy'\n 'Shardul Thakur' 'Sam Curran' 'Arshdeep Singh' 'Nathan Ellis'\n 'Sikandar Raza' 'Rishi Dhawan' 'Rahul Chahar' 'Harpreet Brar'\n 'Kyle Mayers' 'Jaydev Unadkat' 'Krishnappa Gowtham' 'Avesh Khan'\n 'Mark Wood' 'Ravi Bishnoi' 'Khaleel Ahmed' 'Mukesh Kumar'\n 'Chetan Sakariya' 'Axar Patel' 'Kuldeep Yadav' 'Bhuvneshwar Kumar'\n 'Fazalhaq Farooqi' 'Washington Sundar' 'T Natarajan' 'Adil Rashid'\n 'Umran Malik' 'Trent Boult' 'KM Asif' 'Jason Holder'\n 'Ravichandran Ashwin' 'Yuzvendra Chahal' 'Navdeep Saini' 'Mohammed Siraj'\n 'Reece Topley' 'Akash Deep' 'Harshal Patel' 'Karn Sharma'\n 'Michael Bracewell' 'Glenn Maxwell' 'Jason Behrendorff' 'Arshad Khan'\n 'Jofra Archer' 'Piyush Chawla' 'Cameron Green' 'Hrithik Shokeen'\n 'Krunal Pandya' 'Yash Thakur' 'Ben Stokes' 'Moeen Ali' 'RS Hangargekar'\n 'Anrich Nortje' 'Mitchell Marsh' 'David Willey' 'Shahbaz Ahmed'\n 'Suyash Sharma' 'Deepak Hooda' 'Amit Mishra' 'Aiden Markram'\n 'Rovman Powell' 'Sandeep Sharma' 'Murugan Ashwin' 'Sisanda Magala'\n 'Dwaine Pretorius' 'Kumar Kartikeya' 'Lockie Ferguson' 'Marco Jansen'\n 'Mayank Markande' 'Mohit Rathee' 'Wayne Parnell' 'Riley Meredith'\n 'Tilak Varma' 'Mustafizur Rahman' 'Lalit Yadav' 'Akash Singh'\n 'Maheesh Theekshana' 'Kuldeep Sen' 'Adam Zampa' 'Mohit Sharma'\n 'Kagiso Rabada' 'Matthew Short' 'Andre Russell' 'Vijaykumar Vyshak'\n 'Wanindu Hasaranga' 'Yudhvir Singh Charak' 'Arjun Tendulkar'\n 'Duan Jansen' 'Noor Ahmad' 'Matheesha Pathirana' 'Naveen-ul-Haq'\n 'Liam Livingstone' 'Ishant Sharma' 'Kulwant Khejroliya' 'Anukul Roy'\n 'Nitish Rana' 'Mayank Dagar' 'Marcus Stoinis' 'Jayant Yadav'\n 'Rahul Tewatia' 'David Wiese' 'Vaibhav Arora' 'Kuldip Yadav'\n 'Gurnoor Brar' 'Ayush Badoni' 'Harshit Rana' 'Akeal Hosein'\n 'Abhishek Sharma' 'Josh Hazlewood' 'Mahipal Lomror' 'Akash Madhwal'\n 'Kartik Tyagi' 'Raghav Goyal' 'Tristan Stubbs' 'Mohsin Khan'\n 'Swapnil Singh' 'Vivrant Sharma' 'Obed McCoy' 'Chris Jordan' 'Joe Root'\n 'Yudhvir Singh' 'Glenn Phillips' 'Praveen Dubey' 'Nitish Reddy'\n 'Himanshu Sharma']\nTeams  ['Gujarat Titans' 'Chennai Super Kings' 'Kolkata Knight Riders'\n 'Punjab Kings' 'Lucknow Super Giants' 'Delhi Capitals'\n 'Sunrisers Hyderabad' 'Rajasthan Royals' 'Royal Challengers Bangalore'\n 'Mumbai Indians' 'sunrisers Hyderabad']\nCity  ['Ahmedabad' 'Mohali' 'Lucknow' 'Hyderabad' 'Bengaluru' 'Chennai' 'Delhi'\n 'Guwahati' 'Kolkata' 'Lucknow ' 'Mumbai' 'Jaipur' 'Dharamsala']\n\n"}]
    functions = [
        {
            "name": "generate_question",
            "description": "Generates the answer by running the query in dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "question_prompt": {
                        "type": "string",
                        "description": "Enter a question where the answer is either a batsman, bowler, team or a integer"
                    },
                    "pandas_query": {
                        "type": "string",
                        "description": "Enter a valid pandas query that is compatible with mentioned schema and gets the answers to the above question",
                    },
                    "answer_type": {
                        "type": "string",
                        "description": "This should be one of [batsman, bowler, team, out_by]",
                    }
                },
                "required": ["question_prompt", "pandas_query", "answer_type"],
            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    print(response)
    response_message = response["choices"][0]["message"]

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "generate_question": generate_question,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            question_prompt=function_args.get("question_prompt"),
            pandas_query=function_args.get("pandas_query"),
            answer_type=function_args.get("answer_type")
        )
        return function_response


@app.route('/api/python')
def hello_world():
    return generate_question_query()


if __name__ == '__main__':
    app.run()
