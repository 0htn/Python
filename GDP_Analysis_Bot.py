# Import libraries
import pandas as pd 
import scipy
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
# Save excel or csv file with data saved in google drive
url = 'https://raw.githubusercontent.com/jacoblongthon/GDP-Data.csv/main/GDP%20Data%20By%20Country%20CSV.csv'
df1 = pd.read_csv(url)
# List of countries the user can choose from (~30-40 total) 
print('This is a table of 50 countries with GDP Data')
# Saving country values into a list to print out for easy readability
my_list = df1.Country.values
# Format to print the list of countries
fss = '{a[0]:25} {a[1]:25} {a[2]:25} {a[3]:25} {a[4]:25}'
# Printing the countries below
print('\nCountries available to choose from listed below:')
for x in range(10):
    print(fss.format(a = my_list[0 + x*5:5 + x*10]))
print('\n')

# While loop to keep user in until want to leave
while True:
    user_input = int(input('''
-----------------MENU-----------------
1. Summarize country GDP stats
2. Compare 2 countries GDP stats
3. Countries projected GDP
4. Quit 
    -->
'''))
    while user_input not in [1, 2, 3, 4]:
        user_input = int(input('Choose 1, 2, 3, 4 from menu options: '))
        
    if user_input == 1: 
        # User select country. While invalid, ask for valid input
        country_choice = input('Please choose a country:  ')
        while country_choice not in df1.Country.values:
            country_choice = input('Please select a valid country: ')
            #Saving User Input as a variable to use be able to summarize Data
        countryfin = df1.loc[df1['Country'] == country_choice]
        #Formating the Output to make it easier for reader to read
        df_list = countryfin.values.flatten()
        print(f"""      
              Country: {df_list[0]}
              Nominal: {df_list[1]}
              Abbreviated: {df_list[2]}
              GDP Growth: {df_list[3]}
              Population: {df_list[4]}
              Per capita: {df_list[5]}
              Share of World GDP: {df_list[6]}
              """)

        # Allowing user to compare 2 countries GDP data with data viz
    elif user_input == 2:
        # User select first country. While invalid, ask for valid input
        country_one = input('Please select first country: ')
        while country_one not in df1.Country.values:
            country_one = input('Please select a valid country: ')
          # User select second country. While invalid, ask for valid input.
        country_two = input('Please select second country: ')
        while country_two not in df1.Country.values:
            country_two = input('Please select a valid country: ')
        # Saving nominal values and abbreviated names to use later.
        gdp_one = df1.loc[df1['Country'] == country_one, 'Nominal'].item()
        gdp_two = df1.loc[df1['Country'] == country_two, 'Nominal'].item()
        ab_one = df1.loc[df1['Country'] == country_one, 'Abbreviated'].item()
        ab_two = df1.loc[df1['Country'] == country_two, 'Abbreviated'].item()

        # Simple Bar Plot
        plt.figure(figsize=(6, 6))
        x = [country_one, country_two]
        y = [gdp_one, gdp_two]
        z = [ab_one, ab_two]
        plt.yticks(y, " ")
        plots = plt.bar(x,y)

        counts = 0
        for bar in plots.patches:
            plt.annotate(format(z[counts]), (bar.get_x() + bar.get_width() / 2,
                        bar.get_height()- 10), ha='center', va='center', 
                        size=12, xytext=(0, 8),
                        textcoords='offset points')
            # Count increase to add second plot label on bar
            counts += 1
        # Label the graph
        plt.xlabel
        plt.xlabel('Countries')
        plt.ylabel("Nominal GDP ($)")
        plt.title('Country GDP Comparison')
        # Display graph
        plt.show()
    elif user_input == 3:
        # Create new column and Remove unwanted symbols
        df1['Growth'] = df1['GDP Growth'].str.replace('[%, .]', '')
        #Update column from string to numeric
        df1['Growth'] = pd.to_numeric(df1['Growth'])
        # Create another new column and Calculate GDP from Nominal and GDP growth
        df1['GDP'] = df1['Growth'] * df1['Nominal']
        df1['GDP'] = df1['GDP'].floordiv(10000)
        # Plotting the graph
        sns.set(rc = {'figure.figsize': (13,9)})
        gdp_plt = sns.scatterplot(x = 'GDP', y = 'Country', data = df1)
        # Display calculated GDP
        opt = input("""Would you like us to display the table 
        of 50 countries with calculated GDP?: """)
        optl = opt.lower()
        while optl not in ['yes', 'no']:
            optl = input("Please enter a valid response, yes or no: ")
        if optl == 'yes':
            optl = df1[['Country', 'GDP', 'Nominal', 'GDP Growth']]
            print(optl)
        # Display graph
        print('GDP Scatter Plot')
        plt.show()
        
    #if user input is 4
    else:
        break
# Print exit message
print("Thank you for using GDP Bot.")  
