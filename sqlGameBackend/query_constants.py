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