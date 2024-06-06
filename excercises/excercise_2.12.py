import pandas as pd

html_script = '''
<table>
    <thead>
        <tr>
            <th>Sequence</th>
            <th>Country</th>
            <th>Population</th>
            <th>date</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td>China</td>
            <td>1,439,323,776</td>
            <td>1-Dec-2020</td>
        </tr>
        <tr>
            <td>2</td>
            <td>India</td>
            <td>1,380,004,385</td>
            <td>1-Dec-2020</td>
        </tr>
        <tr>
            <td>3</td>
            <td>United States</td>
            <td>331,002,651</td>
            <td>1-Dec-2020</td>
        </tr>
    </tbody>
</table>'''

# Note: parse_dates, is the correct answer, the other available parameter is date_parser which is not included here
# Proof: https://pandas.pydata.org/docs/reference/api/pandas.read_html.html 
# Assertion: https://oxylabs.io/blog/pandas-read-html-tables 
html_parsed = dfs = pd.read_html(html_script, parse_dates=['date'])

df = html_parsed[0]
print(df.info())