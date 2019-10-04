import os
import csv


def main():
    
    # Defines File to be opened and initializes variables
    file = os.path.join("budget_data.csv")
    total_months = 0
    net_prof = 0
    value_list = []
    av_change_list = []
    date_list = []
    inc_max = 0
    dec_max = 0
    
    # Opens file in 'read'
    with open(file, 'r', newline="") as b_file:
        
        # Defines 'reader' as dict. containing all contents of file as strings; automatically recognizes that the first row contains column names
        reader = csv.DictReader(b_file)

        # Iterates over every key:value pair in 'reader'
        for line in reader:
            # Knowing that each row in the file contains data for 1 month, calculating 'total_months' involved applying a simple counter (though I could have also used 'len', I think)
            total_months += 1
            # Using the dict. key of 'Profit/Losses', this reads P/L data (value) of current line and appends the int value to our initialized list
            pro_loss = int(line['Profit/Losses'])
            value_list.append(pro_loss)
            # We replicated the process above but with the 'Date' key
            date_cur = line['Date']
            date_list.append(date_cur)
            # Calculates net profit
            net_prof += pro_loss

        # Iterates over our custom 'value_list' via its index
        for i in range(len(value_list)):
            # Ignores first value in list
            if i == 0:
                continue
            else:
                # Subtracts the current val by the previous val to calculate change per month
                cur_change = value_list[i] - value_list[i - 1]
                # The calculated change gets appended to its own list
                av_change_list.append(cur_change)
                # Checks if the current value of cur_change is less than the value defined as inc_max; if true, inc_max gets cur_change
                if inc_max == 0 or inc_max < cur_change:
                    inc_max = cur_change
                    # Records where in the list a change in inc_max occured, since both lists are ordered the same way
                    date_inc_max = date_list[i]
                # Same as above, except for max decrease and '<' replaced by '>'
                if dec_max == 0 or dec_max > cur_change:
                    dec_max = cur_change
                    date_dec_max = date_list[i]        
        # Calculates the average change in profit month-to-month
        average_pro_loss = round(sum(av_change_list)/(len(av_change_list)), 2)
    
    # Creates new file (or writes over old one) in the current folder
    outfile = os.path.join("financial_report.txt")
    with open(outfile, 'w') as financial_report:
        textwriter = financial_report.write
        # Writes out the report
        textwriter(
            f"\nFinancial Report:\n-------------------\n Total Months: {total_months}\n Net Profits: ${net_prof}\n Average Monthly Change: ${average_pro_loss}\n Greatest Increase in Profits: {date_inc_max}  (${inc_max})\n Greatest Decrease in Profits: {date_dec_max}  (${dec_max})\n")
    # Prints version of the report to user's terminal
    print(
        f"\nFinancial Report:\n-------------------\n Total Months: {total_months}\n Net Profits: ${net_prof}\n Average Monthly Change: ${average_pro_loss}\n Greatest Increase in Profits: {date_inc_max}  (${inc_max})\n Greatest Decrease in Profits: {date_dec_max}  (${dec_max})\n")


if __name__ == "__main__":
    main()