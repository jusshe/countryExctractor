import urllib.request as req
import json
import fileinput
import re

countries = {
    # added
    "Myanmar (Burma)": "MM",
    "USA": "US",
    "Antigua and Barbuda": "AG",

    "Zimbabwe": "ZW",
    "Zambia": "ZM",
    "Yugoslavia": "YU",
    "Yemen": "YE",
    "Western Sahara": "EH",
    "West Bank": "PS",
    "Wallis And Futuna Islands": "WF",
    "Virgin Islands (U.S.)": "VI",
    "Vietnam": "VN",
    "Venezuela": "VE",
    "Vanuatu": "VU",
    "Uzbekistan": "UZ",
    "USSR": "SU",
    "Uruguay": "UY",
    "Unknown": "XX",
    "United States Minor Outlaying Islands": "UM",
    "United States": "US",
    "United Kingdom": "GB",
    "United Arab Emirates": "AE",
    "Ukraine": "UA",
    "Uganda": "UG",
    "Tuvalu": "TV",
    "Turks And Caicos Islands": "TC",
    "Turkmenistan": "TM",
    "Turkey": "TR",
    "Tunisia": "TN",
    "Trinidad And Tobago": "TT",
    "Tonga": "TO",
    "Tokelau": "TK",
    "Togo": "TG",
    "Thailand": "TH",
    "Tanzania": "TZ",
    "Tajikistan": "TJ",
    "Taiwan": "TW",
    "Syria": "SY",
    "Switzerland": "CH",
    "Sweden": "SE",
    "Swaziland": "SZ",
    "Svalbard And Jan Mayen Islands": "SJ",
    "Suriname": "SR",
    "Sudan": "SD",
    "St. Vincent And The Grenadines": "VC",
    "St. Lucia": "LC",
    "St. Kitts And Nevis": "KN",
    "Sri Lanka": "LK",
    "Spain": "ES",
    "South Sudan": "SS",
    "South Korea": "KR",
    "South Georgia and S.Sandwich Is.": "GS",
    "South Africa": "ZA",
    "Somalia": "SO",
    "Solomon Islands": "SB",
    "Slovenia": "SI",
    "Slovak Republic": "SK",
    "Sint Maarten": "SX",
    "Singapore": "SG",
    "Sierra Leone": "SL",
    "Seychelles": "SC",
    "Serbia And Montenegro": "CS",
    "Serbia": "RS",
    "Senegal": "SN",
    "Saudi Arabia": "SA",
    "Sao Tome And Principe": "ST",
    "San Marino": "SM",
    "Samoa": "WS",
    "Saint Pierre And Miquelon": "PM",
    "Saint Martin": "MF",
    "Saint Helena": "SH",
    "Saint Barthelemy": "BL",
    "Rwanda": "RW",
    "Russia": "RU",
    "Romania": "RO",
    "Reunion": "RE",
    "Qatar": "QA",
    "Puerto Rico": "PR",
    "Portugal": "PT",
    "Poland": "PL",
    "Pitcairn": "PN",
    "Philippines": "PH",
    "Peru": "PE",
    "Paraguay": "PY",
    "Papua New Guinea": "PG",
    "Panama -- Canal Zone": "PZ",
    "Panama": "PA",
    "Palau": "PW",
    "Pakistan": "PK",
    "Oman": "OM",
    "Norway": "NO",
    "Northern Mariana Islands": "MP",
    "North Korea": "KP",
    "Norfolk Island": "NF",
    "Niue": "NU",
    "Nigeria": "NG",
    "Niger": "NE",
    "Nicaragua": "NI",
    "New Zealand": "NZ",
    "New Caledonia": "NC",
    "Netherlands Antilles": "AN",
    "Netherlands": "NL",
    "Nepal": "NP",
    "Nauru": "NR",
    "Namibia": "NA",
    "Myanmar": "MM",
    "Mozambique": "MZ",
    "Morocco": "MA",
    "Montserrat": "MS",
    "Montenegro": "ME",
    "Mongolia": "MN",
    "Monaco ": "MC",
    "Moldova": "MD",
    "Micronesia": "FM",
    "Mexico": "MX",
    "Mayotte": "YT",
    "Mauritius": "MU",
    "Mauritania": "MR",
    "Martinique": "MQ",
    "Marshall Islands": "MH",
    "Malta": "MT",
    "Mali": "ML",
    "Maldives": "MV",
    "Malaysia": "MY",
    "Malawi": "MW",
    "Madagascar": "MG",
    "Macedonia": "MK",
    "Macao": "MO",
    "Luxembourg": "LU",
    "Lithuania": "LT",
    "Liechtenstein": "LI",
    "Libya": "LY",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lebanon": "LB",
    "Latvia": "LV",
    "Laos": "LA",
    "Kyrgyz Republic": "KG",
    "Kuwait": "KW",
    "Kiribati": "KI",
    "Kenya": "KE",
    "Kazakhstan": "KZ",
    "Jordan": "JO",
    "Jersey - C.I.": "JE",
    "Japan": "JP",
    "Jamaica": "JM",
    "Ivory Coast": "CI",
    "Italy": "IT",
    "Israel": "IL",
    "Isle Of Man": "IM",
    "Ireland": "IE",
    "Iraq": "IQ",
    "Iran": "IR",
    "Indonesia": "ID",
    "India": "IN",
    "Iceland": "IS",
    "Hungary": "HU",
    "Hong Kong": "HK",
    "Honduras": "HN",
    "Holy See (Vatican City State)": "VA",
    "Heard And Mcdonald Islands": "HM",
    "Haiti": "HT",
    "Guyana": "GY",
    "Guinea-Bissau": "GW",
    "Guinea": "GN",
    "Guernsey - C.I.": "GG",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guadeloupe": "GP",
    "Grenada": "GD",
    "Greenland": "GL",
    "Greece": "GR",
    "Gibraltar": "GI",
    "Ghana": "GH",
    "Germany": "DE",
    "Georgia": "GE",
    "Gambia": "GM",
    "Gabon": "GA",
    "French Southern Territories": "TF",
    "French Polynesia": "PF",
    "French Guiana": "GF",
    "France": "FR",
    "Finland": "FI",
    "Fiji": "FJ",
    "Faroe Islands": "FO",
    "Falkland Islands (Malvinas)": "FK",
    "Ethiopia": "ET",
    "Estonia": "EE",
    "Eritrea": "ER",
    "Equatorial Guinea": "GQ",
    "El Salvador": "SV",
    "Egypt": "EG",
    "Ecuador": "EC",
    "East Timor": "TL",
    "Dominican Republic": "DO",
    "Dominica": "DM",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Czech Republic": "CZ",
    "Cyprus": "CY",
    "Curacao": "CW",
    "Cuba": "CU",
    "Croatia": "HR",
    "Costa Rica": "CR",
    "Cook Islands": "CK",
    "Congo (Republic Of)": "CG",
    "Congo - Dem. Rep. (Zaire)": "CD",
    "Democratic Republic of the Congo": "CD",
    "Comoros": "KM",
    "Colombia": "CO",
    "Cocos (Keeling) Islands": "CC",
    "Christmas Island": "CX",
    "China": "CN",
    "Chile": "CL",
    "Chad": "TD",
    "Central African Republic": "CF",
    "Cayman Islands": "KY",
    "Cape Verde": "CV",
    "Canada": "CA",
    "Cameroon": "CM",
    "Cambodia": "KH",
    "Burundi": "BI",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Brunei": "BN",
    "British Virgin Islands": "VG",
    "British Indian Ocean Territory": "IO",
    "Brazil": "BR",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Bosnia-Herzegovina": "BA",
    "Bonaire Sint Eustatius and Saba": "BQ",
    "Bolivia": "BO",
    "Bhutan": "BT",
    "Bermuda": "BM",
    "Benin": "BJ",
    "Belize": "BZ",
    "Belgium": "BE",
    "Belarus": "BY",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Bahrain": "BH",
    "Bahamas": "BS",
    "Azerbaijan": "AZ",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Armenia": "AM",
    "Argentina": "AR",
    "Antigua And Barbuda": "AG",
    "Antarctica": "AQ",
    "Anguilla": "AI",
    "Angola": "AO",
    "Andorra": "AD",
    "American Samoa": "AS",
    "Algeria": "DZ",
    "Albania": "AL",
    "Aland Island": "AX",
    "Afghanistan": "AF"
}

firstHalf = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="
secondHalf = "&inputtype=textquery&fields=formatted_address&key="

# for each line in the csv stdin...
for line in fileinput.input():
    done = False
    strArr = []
    index = 0
    # Fill array, one index per address line
    for i in range(4):
        removed = False
        # csv element surrounded
        if line.find('"', index) == index:
            if line[index + 2] == "/":
                if line[index + 1] == "3" or line[index + 1] == "7":
                    print(line[index + 3: index + 5])
                    done = True
                    break
                removed = True
                index += 2
            strArr.append(line[index + 1:line.find('"', index + 1)])
            index = line.find('"', index + 1) + 2
        # element not surrounded by quotes
        else:
            if line[index + 1] == "/":
                if line[index + 1] == "3" or line[index + 1] == "7":
                    print(line[index + 3: index + 5])
                    done = True
                    break
                removed = True
                index += 2
            if line.find(",", index) == -1:
                strArr.append(line[index:len(line) - 2])
                break
            strArr.append(line[index:line.find(",", index)])
            index = line.find(",", index) + 1
        # place space if line is too small to spill to next
        if i < 3:
            cap = 35
            if removed:
                cap = 33
            if len(strArr[-1]) < cap:
                strArr[-1] += " "
        while len(line) > index and line[index] == ",":
            index += 1
            i += 1
            if i == 4:
                break
        if index+1 >= len(line):
            break

    if done:
        continue

    length = len(strArr)

    for i in range(length):
        strArr[i] = strArr[i].replace(" ", "%20")

    for i in range(length):
        str = ""
        for j in range(i, length):
            str += strArr[j]

        url = firstHalf + str + secondHalf
        results = req.urlopen(url)

        resultsAsJSON = json.load(results)["candidates"]

        if resultsAsJSON:
            address = resultsAsJSON[0]["formatted_address"]
            rightComma = address.rfind(",") + 1
            country = address[rightComma:]
            trimmedCountry = "".join([j for j in country if not j.isdigit()])
            trimmedCountry = trimmedCountry.strip(" ")
            if trimmedCountry in countries.keys():
                print(countries[trimmedCountry])
            # if the country is not in the country:countryCode dictionary, check for JCK characters
            else:
                if re.search("[\u3040-\u30ff]", trimmedCountry):
                    print("JP")
                elif re.search("[\u4e00-\u9FFF]", trimmedCountry):
                    print("CN")
                else:
                    print("")
            done = True
            break

    if not done:
        print("No Address")
