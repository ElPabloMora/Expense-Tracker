import argparse
from commands.commands import *
 
def  main():
    parser = argparse.ArgumentParser(description='Expense Tracker')
    subparsers = parser.add_subparsers(dest='command')
    
    add_parser = subparsers.add_parser('add',  help='Add a new task')
    add_parser.add_argument('--description', type=str, help="Description")
    add_parser.add_argument('--amount', type=int, help='Amount')

    summary_parser = subparsers.add_parser('summary', help='')
    summary_parser.add_argument('--month',type=int, help='Summary')
    
    list_parser = subparsers.add_parser('list', help='')
 
    delete_parser = subparsers.add_parser('delete', help='Delete a task by id')
    delete_parser.add_argument('--id', type=int, help='Identification')
    
    args = parser.parse_args()

    if args.command == 'add':
        add_expenses(args.description,args.amount)
    elif args.command == 'summary':
        if args.month:
            sumamry_month(args.month)
        else: 
            sumamry()
    elif args.command == 'list':
        list_expense()
    elif args.command == 'delete':
        delete_expense(args.id)

if __name__ == '__main__':
    main()