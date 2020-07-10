import csv
from collections import Counter

class Survery_Analysis(object):

    def get_hobbiest_programmer_percent(self):
        # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)

            # Initilizing the counter
            counts = Counter()

            # reading the csv and increasing the counter as per answer for Hobbyist Programmer = Yes/No
            for line in csv_reader:
                counts[line['Hobbyist']] += 1

            yes_percent = round(((counts['Yes']/(counts['Yes']+counts['No']))*100),2)
            no_percent = round(((counts['No']/(counts['Yes']+counts['No']))*100),2)
            ##print the %
            print("Hobbyist Programmer - Yes = " + str(yes_percent) + '%')
            print("Hobbyist Programmer - No = " + str(no_percent) +'%')

    def top_5_popular_languages(self):
        total = 0
        
       # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            
            # Initilizing the counter
            language_counter = Counter()
            
            # reading the csv and increasing the counter as per answer for Hobbyist Programmer = Yes/No
            for line in csv_reader:
                languages = line['LanguageWorkedWith'].split(';')
                
                # Updating the respective language counter as per response from csv file
                language_counter.update(languages)
                
                #getting the total number of responses from csv file        
                total+=1
            
        for language, value in language_counter.most_common(5):
            language_pct = (value/total)*100
        
            print(f'{language}: {round(language_pct,2)}%')
    
    def top_5_country_responded(self):
        # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            
            # Initilizing the counter
            country_counter = Counter()

            for country in csv_reader:
                country_counter[country['Country']]+=1
                
            print(country_counter.most_common(5))

    def response_by_dev_type(self):
        # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            
            # Initilizing the counter
            dev_type_counter = Counter()

            for developer in csv_reader:
                dev_type_counter[developer['DevType']]+=1
                
            
        for developer in dev_type_counter.most_common(10):    
            print(str(developer).replace("'Developer,",""))    

    def top_5_os(self):
        # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            
            # Initilizing the counter
            os_type_counter = Counter()

            for system in csv_reader:
                os_type_counter[system['OpSys']]+=1

        for os in os_type_counter:
            print(str(os) + '=' + str(os_type_counter[os]))
                    
    def top_5_social_media(self):
        total = 0
        # reading the csv file
        with open(r'Survey_Data/survey_results_public.csv', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            
            # Initilizing the counter
            sm_type_counter = Counter()

            for socialmedia in csv_reader:
                sm_type_counter[socialmedia['SocialMedia']]+=1
                total+=1
            
        for site, value in sm_type_counter.most_common(5):
            sm_percent = round(((value/total)*100),2)
            sm_type_counter[site] = sm_percent
            print(site + '-' + str(sm_percent) +'%')    
    
    
def main():
    analysis = Survery_Analysis()
    analysis.top_5_social_media()


if __name__ == "__main__":
    main()
