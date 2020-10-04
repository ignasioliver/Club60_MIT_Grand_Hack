# Club 60+
Porject developed at MIT GrandHack Medicine by **team_c_073**:
- Ananda Ciabotti
- Dorrie Bartels
- Tuneer Biswas
- Kavya Bhargava
- Ignasi Oliver

## Important considerations:
This is a very primitive MVP in the sense that the UX flow is done and can be tested -go to Installation-, the DB is designed created but it is not connected, so changes are not saved.
The following steps to develop is to integrate it to FHIR R4 Patient Resource, so external resources and platform could be implemented into the workflow -such as healthcare provider's systems- and make it escalable. For that, we have set up InterSystems instances on AWS. If you want to take a look, the links are as follow:
- FHIRAPIDevPortal: [http://3.218.143.59:8003/default/documentation](http://3.218.143.59:8003/default/documentation)
- IRISPortal: [http://3.218.143.59:9088/csp/sys/%25CSP.Portal.Home.zen](http://3.218.143.59:9088/csp/sys/%25CSP.Portal.Home.zen)


## Test it live:

## Installation
To install **Club 60+** in your system, make sure [Python](https://www.python.org/downloads/) is installed.
1. [Clone/fetch/pull](https://help.github.com/en/articles/cloning-a-repository) the repository to your system.
2. It is recommended to run the application through a [virtual environment](https://docs.python.org/3/tutorial/venv.html). For example, [virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). In a Linux a terminal:
    - `pip3 install virtualenv`
    - `virtualenv venv`
    - `source venv/bin/activate`
3. Install the requirements:
    - `pip3 install -r requirements.txt`<br>
4. Run the application:
    - `python3 wsgi.py`
5. Open a web browser and go to [http://localhost:5000](http://localhost:5000).


