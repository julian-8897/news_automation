import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--lower_date',
                        type=str,
                        help='Lower bound for date range',
                        default='10/28/2022')

    parser.add_argument('--upper_date',
                        type=str,
                        help='Upper bound for date range',
                        default='10/30/2022')

    parser.add_argument('--key_words',
                        nargs='+',
                        help='List of Search Keywords',
                        required=True)

    parser.add_argument('--n_pages',
                        type=int,
                        help='Specified number of pages to fetch articles',
                        default=1)

    return parser.parse_args()