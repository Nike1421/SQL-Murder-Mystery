queries = [
    '''
SELECT *
FROM crime_scene_report
WHERE city = "SQL City"
ORDER BY date;
''',
    '''
SELECT *
FROM person
WHERE name like '%Morty%'  AND address_street_name = "Northwestern Dr";
''',
    '''
SELECT *
FROM person
WHERE name like '%Annabel%' AND address_street_name = "Franklin Ave";
''',
    '''
SELECT *
FROM interview
WHERE person_id = 14887 OR person_id = 16371;
''',
    '''
SELECT *
FROM get_fit_now_check_in 
WHERE membership_id like "%48Z%" AND check_in_date = 20180109 
order by check_in_date;
''',
    '''
SELECT *
FROM drivers_license
WHERE plate_number like "%H42W%";
''',
    '''
SELECT *
FROM person
WHERE license_id = "423327" OR license_id = "664760";
''',
    '''
SELECT *
FROM get_fit_now_member
WHERE person_id = "51739" OR person_id = "67318";
''',

]

questions = [
    "There's been a Murder in SQL City!\nA crime has taken place and I need\nyour help. I have given you the crime\nscene report, but you somehow lost it.\nYou vaguely remember that the murder\noccurred sometime on Jan 15, 2018\nand that it took place in SQL City.\nStart by retrieving the corresponding\ncrime scene report from the police\ndepartment's database.",
    "The security footage shows\nthat there were two witnesses.\nThe first witness, Mr. Morty lives in\nthe last house on\"Northwestern\nDr\". Let us look for the details\nof the first witness.",
    "The second witness,\nAnnabel, lives somewhere\n on \"Franklin Ave\". Now,\nlet's get her details.",
    "Now, let's take a\nlook at the interviews\nof the witnesses taken\nafter the murder...",
    "All right, there are two clues.\nThe killer is a male and holds\na Gold Membership in the Gym.\nHis ID starts with \'48Z\' and he\nwas working out in the gym on\nJan. 9. He left in a car with a\nnumber plate H42W. Check the\ngym database with these details.",
    "There are two gym members\nwith matching membership IDs.\nNow, let's check the car details\nsimilarly...",
    "Good job! There are two\nmales having cars with plate\nnumbers containing \'H42W\'.\nNow, check the personal\ndetails of them both...",
    "Now, of these two,\nwho is a member of the Gym?\nFind that out please!",
    "Congratulations, you found\nthe murderer - Jeremy Bowers.\nBoth the membership ID and status\nmatch as per the information\nwe found earlier.",
]

hints = [
    "Hints : Find all crime scene reports in 'SQL City' and sort them by date.",
    "Hints : Find all persons on 'Northwestern Dr' where street name is 'Northwestern Dr'. Note down the ID, It might be useful in further deduction.",
    "Hints : Find all persons on 'Annabel' where street name is 'Franklin Ave'.",
    "Hints : Retrieve all interviews for persons with ID 14887 or 16371.",
    "Hints : Retrieve all check-ins on Jan 9, 2018 for members with ID containing '48Z', and sort them by date.",
    "Hints : Retrieve all driver's licenses with a plate number containing 'H42W'.",
    "Hints : Retrieve all persons with license IDs 423327 or 664760",
    "Hints : Retrieve all members with person IDs 51739 or 67318."
]
