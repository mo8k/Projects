
prices = []
with open('ticket.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    
    infile.readline()
    
    for line in infile:
        cleaned_line = line.strip()
        parts = cleaned_line.split()
        price_string = parts[1]
        price_float = float(price_string)
        prices.append(price_float)

    if prices:
        count = len(prices)
        max_price = max(prices)
        min_price = min(prices)
        average_price = sum(prices) / count

        outfile.write("**************************************\n")
        outfile.write("          TICKET REPORT\n")
        outfile.write("**************************************\n")
        outfile.write(f"There are {count} tickets in the database.\n")

        outfile.write(f"The Maximum Ticket price is ${max_price:.2f}.\n")
        outfile.write(f"The minimum Ticket price is ${min_price:.2f}.\n")
        outfile.write(f"The average Ticket Price is ${average_price:.2f}.\n")
        outfile.write("Thank you for using our ticket system!\n")
    else:
        outfile.write("**************************************\n")
        outfile.write("        TICKET REPORT\n")
        outfile.write("**************************************\n")
        outfile.write("No tickets found in the input file.\n")
        outfile.write("Thank you for using our ticket system!\n")

print("Report 'output.txt' has been created successfully.")