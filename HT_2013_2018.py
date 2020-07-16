
import matplotlib.pyplot as plt

#Using the info from sql queries, making a graph to plot cases by state

states = ['TX','MN','IL','AZ','OK','TN','FL','NV','LA','MO','CO','SC','AK',
          'WI','WA','MD','MA','WY','IN','OH','RI','AR','HI','ND','CT','DE',
          'MI','KY','KS','MT','NJ','UT','VT']

HT_cases = [529,275,115,81,76,74,69,59,56,47,41,24,23,22,19,16,10,10,9,8,7,6,6,
            6,5,5,5,3,2,2,1,1,1]


plt.figure(dpi=1200)
ax = plt.subplot()
ax.set_xticks(range(len(states)))
ax.set_xticklabels(states,fontsize = 'small', rotation = 90)
plt.bar(range(len(states)), HT_cases, color='green')
plt.title("Human Traffic Cases Per State")
plt.xlabel('State')
plt.ylabel('Number of Cases')
plt.subplots_adjust(bottom=0.25)

plt.savefig('HT_2013_2018_per_state.png', dpi = 1200)
plt.show()
plt.clf()

#Using Texas data to make a pie chart of percent solved, false, unsolved
tex_report = 1211
tex_false_report = 35
tex_solved = 429
tex_per_solv = tex_solved/tex_report * 100
tex_per_false = tex_false_report/tex_report * 100
tex_per_unsolv = 100 - (tex_per_solv + tex_per_false)

tex_labels = ['HT SOLVED', "HT UNSOLVED", "HT FALSE REPORT"]
tex_values = [tex_per_solv, tex_per_unsolv, tex_per_false]

colors = ['lightcoral', 'lightseagreen', 'lightskyblue']
explode = (0.0, 0.05, 0.0)

plt.figure(dpi=1200)
plt.subplot(121)
plt.pie(tex_values, explode = explode, colors = colors, startangle = 345, autopct='%1.1f%%', pctdistance=1.25)
plt.title('Human Traffic Cases - Texas')
plt.legend(tex_labels, loc='upper left', fontsize = 'x-small')

#All US data to show percent solved, unsolved, false
us_report = 4040
us_false_report = 161
us_solved = 1745
us_per_solv = us_solved/us_report * 100
us_per_false = us_false_report/us_report * 100
us_per_unsolv = 100 - (us_per_solv + us_per_false)

us_labels = ['HT SOLVED', "HT UNSOLVED", "HT FALSE REPORT"]
us_values = [us_per_solv, us_per_unsolv, us_per_false]

plt.subplot(122)
plt.pie(us_values, explode = explode, colors = colors, startangle = 345, autopct='%1.1f%%', pctdistance=1.25)
plt.title('Human Traffic Cases - US')
plt.legend(us_labels, loc='upper left', fontsize = 'x-small')


plt.savefig('HT_2013_2018_Tex_US_Comp.png', dpi = 1200)
plt.show()
plt.clf