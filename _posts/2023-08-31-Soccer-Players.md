---
toc: False
comments: False
layout: post
title: Favorite Soccer Players
description: A table of all my favorite soccer players
courses: {'compsci': {'week': 2}}
type: hacks
---

<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Player Number</th>
                <th>Position</th>
                <th>Country</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Lionel Messi</td>
                <td>10</td>
                <td>Striker</td>
                <td>Argentina</td>
            </tr>
            <tr>
                <td>Christiano Ronaldo</td>
                <td>7</td>
                <td>Striker</td>
                <td>Portugal</td>
            </tr>
            <tr>
                <td>Robert Lewandowski</td>
                <td>9</td>
                <td>Striker</td>
                <td>Poland</td>
            </tr>
            <tr>
                <td>Kylian Mbappé</td>
                <td>10</td>
                <td>Striker</td>
                <td>France</td>
            </tr>
            <tr>
                <td>Sergio Ramos</td>
                <td>4</td>
                <td>Center Back</td>
                <td>Spain</td>
            </tr>
            <tr>
                <td>Neymar Jr.</td>
                <td>10</td>
                <td>Striker</td>
                <td>Brazil</td>
            </tr>
            <tr>
                <td>Kevin De Bruyne</td>
                <td>17</td>
                <td>Center Mid</td>
                <td>Belgium</td>
            </tr>
            <tr>
                <td>Erling Haaland</td>
                <td>9</td>
                <td>Striker</td>
                <td>Norway</td>
            </tr>
            <tr>
                <td>Virgil Van Dijk</td>
                <td>4</td>
                <td>Center Back</td>
                <td>Netherlands</td>
            </tr>
            <tr>
                <td>Mohamed Salah</td>
                <td>11</td>
                <td>Right Winger</td>
                <td>Egypt</td>
            </tr>
            <tr>
                <td>Harry Kane</td>
                <td>9</td>
                <td>Striker</td>
                <td>England</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>
