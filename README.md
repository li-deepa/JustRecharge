<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        .success {
            color: green;
        }
        .failure {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Automation Test Dashboard</h1>
    <p>Below is the summary of the automation test results:</p>
    <table>
        <thead>
            <tr>
                <th>Test Case</th>
                <th>Status</th>
                <th>Execution Time</th>
            </tr>
        </thead>
        <tbody id="testResults">
            <!-- Rows will be populated by JavaScript -->
        </tbody>
    </table>

    <script>
        // Example data, replace with actual data source
        const testReport = [
            { testCase: "Login Test", status: "Success", executionTime: "5s" },
            { testCase: "Signup Test", status: "Failure", executionTime: "8s" },
            { testCase: "Logout Test", status: "Success", executionTime: "3s" }
        ];

        const tableBody = document.getElementById("testResults");

        testReport.forEach(test => {
            const row = document.createElement("tr");

            const testCaseCell = document.createElement("td");
            testCaseCell.textContent = test.testCase;

            const statusCell = document.createElement("td");
            statusCell.textContent = test.status;
            statusCell.classList.add(test.status === "Success" ? "success" : "failure");

            const executionTimeCell = document.createElement("td");
            executionTimeCell.textContent = test.executionTime;

            row.appendChild(testCaseCell);
            row.appendChild(statusCell);
            row.appendChild(executionTimeCell);

            tableBody.appendChild(row);
        });
    </script>
</body>
</html>
