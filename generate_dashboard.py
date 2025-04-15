import re
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from bs4 import BeautifulSoup
import os
from collections import defaultdict

def parse_log_file(log_file_path):
    """Parse a log file and extract test execution data"""
    test_data = defaultdict(list)
    current_test = None
    
    with open(log_file_path, 'r') as f:
        for line in f:
            # Match test start lines
            test_start_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) :INFO :(test_\w+) :', line)
            if test_start_match:
                timestamp_str, current_test = test_start_match.groups()
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
                test_data[current_test].append({
                    'timestamp': timestamp,
                    'message': line[len(timestamp_str)+8:].strip(),
                    'status': 'INFO'
                })
            # Match error lines
            elif 'ERROR' in line or 'FAIL' in line:
                error_match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) :(ERROR|FAIL) :', line)
                if error_match and current_test:
                    timestamp_str, error_level = error_match.groups()
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
                    test_data[current_test].append({
                        'timestamp': timestamp,
                        'message': line[len(timestamp_str)+8:].strip(),
                        'status': error_level
                    })
    
    return test_data

def parse_html_report(report_path):
    """Parse the HTML report to extract test results"""
    with open(report_path, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    results = {}
    
    # Find all test sections
    test_sections = soup.find_all('h3')
    for section in test_sections:
        test_name = section.text.strip()
        pre_tag = section.find_next_sibling('pre')
        if pre_tag:
            log_entries = pre_tag.text.strip().split('\n')
            results[test_name] = log_entries
    
    return results

def analyze_test_data(log_data, html_data):
    """Combine and analyze data from log files and HTML report"""
    test_stats = {}
    
    # Process log data
    for test_name, entries in log_data.items():
        executions = len([e for e in entries if 'starting' in e['message'].lower()])
        failures = len([e for e in entries if e['status'] in ['ERROR', 'FAIL']])
        test_stats[test_name] = {
            'executions': executions,
            'failures': failures,
            'failure_rate': failures / executions if executions > 0 else 0,
            'last_execution': max([e['timestamp'] for e in entries]) if entries else None,
            'log_entries': entries
        }
    
    # Process HTML data
    for test_name, entries in html_data.items():
        if test_name not in test_stats:
            test_stats[test_name] = {
                'executions': 0, 
                'failures': 0, 
                'failure_rate': 0,
                'last_execution': None
            }
        
        failures = len([e for e in entries if 'error' in e.lower() or 'fail' in e.lower()])
        test_stats[test_name]['html_failures'] = failures
        test_stats[test_name]['html_entries'] = entries
    
    return test_stats

def generate_dashboard(test_stats):
    """Generate an interactive HTML dashboard"""
    # Prepare data for visualizations
    df = pd.DataFrame.from_dict(test_stats, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Test'}, inplace=True)
    
    # Ensure all required columns exist
    required_columns = ['executions', 'failures', 'failure_rate', 'last_execution']
    for col in required_columns:
        if col not in df.columns:
            df[col] = 0
    
    # Calculate failure rate if not already present
    if 'failure_rate' not in df.columns:
        df['failure_rate'] = df['failures'] / df['executions'].replace(0, 1)  # Avoid division by zero
    
    # Create visualizations
    fig1 = px.bar(df, 
                 x='Test', 
                 y='failures',
                 title='Test Failure Counts',
                 color='failures',
                 color_continuous_scale='RdYlGn_r')
    
    fig2 = px.bar(df,
                 x='Test',
                 y='failure_rate',
                 title='Failure Rate by Test',
                 color='failure_rate',
                 color_continuous_scale='RdYlGn_r')
    
    # Timeline data
    timeline_data = []
    for test, stats in test_stats.items():
        if 'log_entries' in stats:
            for entry in stats['log_entries']:
                timeline_data.append({
                    'Test': test,
                    'Timestamp': entry['timestamp'],
                    'Date': entry['timestamp'].date(),
                    'Status': entry['status'],
                    'Message': entry['message']
                })
    
    timeline_df = pd.DataFrame(timeline_data)
    if not timeline_df.empty:
        timeline_df['Count'] = 1
        timeline_agg = timeline_df.groupby(['Date', 'Test']).count()['Count'].unstack().fillna(0)
        fig3 = px.line(timeline_agg, 
                      x=timeline_agg.index, 
                      y=timeline_agg.columns,
                      title='Test Execution Timeline',
                      labels={'value': 'Execution Count', 'variable': 'Test', 'Date': 'Date'})
    else:
        fig3 = go.Figure()
        fig3.update_layout(title='No timeline data available')
    
    # Recent activity
    recent_activity = timeline_df.sort_values('Timestamp', ascending=False).head(10) if not timeline_df.empty else pd.DataFrame()
    
    # Generate table rows safely
    table_rows = []
    for _, row in df.iterrows():
        table_rows.append(f"""
        <tr>
            <td>{row['Test']}</td>
            <td>{row['executions']}</td>
            <td>{row['failures']}</td>
            <td>{row['failure_rate'] * 100:.1f}%</td>
            <td>{row['last_execution'] if pd.notna(row['last_execution']) else 'N/A'}</td>
        </tr>
        """)
    
    # Create HTML dashboard
    dashboard = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Test Automation Dashboard</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .dashboard-section { margin-bottom: 30px; padding: 20px; background: white; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            .plot-container { width: 100%; margin-bottom: 20px; }
            .stat-card { text-align: center; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
            .stat-value { font-size: 24px; font-weight: bold; }
            .stat-title { font-size: 14px; color: #666; }
            .failure-card { background-color: #ffebee; }
            .success-card { background-color: #e8f5e9; }
            .info-card { background-color: #e3f2fd; }
            table { width: 100%; }
            .table-responsive { overflow-x: auto; }
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <h1 class="my-4">Test Automation Dashboard</h1>
            
            <div class="row mb-4">
                <div class="col-md-4">
                    <div class="stat-card info-card">
                        <div class="stat-title">Total Tests</div>
                        <div class="stat-value">""" + str(len(test_stats)) + """</div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stat-card failure-card">
                        <div class="stat-title">Total Failures</div>
                        <div class="stat-value">""" + str(df['failures'].sum()) + """</div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stat-card success-card">
                        <div class="stat-title">Success Rate</div>
                        <div class="stat-value">""" + "{:.1f}".format(100 - (df['failures'].sum() / df['executions'].sum() * 100 if df['executions'].sum() > 0 else 0)) + """%</div>
                    </div>
                </div>
            </div>
            
            <div class="dashboard-section">
                <h2>Test Overview</h2>
                <div class="row">
                    <div class="col-md-6">
                        <div id="failureCountChart" class="plot-container"></div>
                    </div>
                    <div class="col-md-6">
                        <div id="failureRateChart" class="plot-container"></div>
                    </div>
                </div>
            </div>
            
            <div class="dashboard-section">
                <h2>Execution Timeline</h2>
                <div id="timelineChart" class="plot-container"></div>
            </div>
            
            <div class="dashboard-section">
                <h2>Test Details</h2>
                <div class="table-responsive">
                    <table class="table table-striped table-hover">
                        <thead class="table-light">
                            <tr>
                                <th>Test</th>
                                <th>Executions</th>
                                <th>Failures</th>
                                <th>Failure Rate</th>
                                <th>Last Execution</th>
                            </tr>
                        </thead>
                        <tbody>
                            """ + "".join(table_rows) + """
                        </tbody>
                    </table>
                </div>
            </div>
            
            <div class="dashboard-section">
                <h2>Recent Activity</h2>
                <div class="table-responsive">
                    <table class="table table-striped table-hover">
                        <thead class="table-light">
                            <tr>
                                <th>Timestamp</th>
                                <th>Test</th>
                                <th>Status</th>
                                <th>Message</th>
                            </tr>
                        </thead>
                        <tbody>
                            """ + (
                                "".join([
                                    """
                                    <tr>
                                        <td>""" + str(row['Timestamp']) + """</td>
                                        <td>""" + row['Test'] + """</td>
                                        <td><span class="badge """ + ('bg-danger' if row['Status'] in ['ERROR', 'FAIL'] else 'bg-success') + """">""" + row['Status'] + """</span></td>
                                        <td>""" + row['Message'][:100] + ('' if len(row['Message']) <= 100 else '...') + """</td>
                                    </tr>
                                    """ for _, row in recent_activity.iterrows()
                                ]) if isinstance(recent_activity, pd.DataFrame) and not recent_activity.empty else """
                                <tr><td colspan="4" class="text-center">No recent activity data</td></tr>
                            """) + """
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <script>
            // Render Plotly charts
            var failureCountChart = """ + fig1.to_json() + """;
            Plotly.newPlot('failureCountChart', failureCountChart.data, failureCountChart.layout);
            
            var failureRateChart = """ + fig2.to_json() + """;
            Plotly.newPlot('failureRateChart', failureRateChart.data, failureRateChart.layout);
            
            var timelineChart = """ + fig3.to_json() + """;
            Plotly.newPlot('timelineChart', timelineChart.data, timelineChart.layout);
        </script>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return dashboard

def main():
    # Configuration - update these paths as needed
    log_file_path = 'logfile.log'  # Path to your log file
    report_path = 'report.html'          # Path to your HTML report
    
    # Parse data sources
    log_data = parse_log_file(log_file_path) if os.path.exists(log_file_path) else {}
    html_data = parse_html_report(report_path) if os.path.exists(report_path) else {}
    
    # Analyze and combine data
    test_stats = analyze_test_data(log_data, html_data)
    
    # Generate dashboard
    dashboard_html = generate_dashboard(test_stats)
    
    # Save the dashboard
    with open('test_dashboard.html', 'w') as f:
        f.write(dashboard_html)
    
    print("Dashboard generated successfully! Open 'test_dashboard.html' in your browser.")

if __name__ == "__main__":
    main()