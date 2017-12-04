import requests
from datetime import datetime
from exceptions import APIError

class DEARSystemsAPI(object):
	"""API wrapper for DEARSystems, must include Account ID and Key"""
	def __init__(self, acct_id, acct_key):
		super(DEARSystemsAPI, self).__init__()
		self.acct_id = acct_id
		self.acct_key = acct_key

		self.headers = {"api-auth-accountid": self.acct_id, "api-auth-applicationkey": self.acct_key}
		self.url = "https://inventory.dearsystems.com/ExternalApi/"
		auth_url = self.url + "Me"

		self.r = requests.get(auth_url, headers=self.headers)

		if self.r.status_code == 403:
			raise APIError("Authentication failed. Please check your credentials!")


	def __repr__(self):
		return "<api object>"

	def me(self):
		"""Get information about the company"""
		return self.r.json()

	def attribute_sets(self, uuid=None, name=None):
		"""Returns sets of attributes, optional ID and name"""
		a_url = self.url + "AttributeSets"
		payload = {}
		if uuid:
			payload["ID"] = uuid
		if name:
			payload["Name"] = name
		self.r = requests.get(a_url, headers=self.headers, params=payload)
		return self.r.json()

	def chart_of_accounts(self, code=None, name=None, className=None, status=None, accept_payments=False, system_account=False):
		"""Returns details of accounts from chart"""
		chart_url = self.url + "ChartOfAccounts"
		payload = {}
		if code:
			payload["Code"] = code
		if name:
			payload["Name"] = name
		if className:
			payload["Class"] = className
		if status:
			payload["Status"] = status
		if accept_payments:
			payload["AcceptPayments"] = True
		if system_account:
			payload["SystemAccount"] = True
		self.r = requests.get(chart_url, headers=self.headers, params=payload)
		return self.r.json()

	def customers(self, uuid=None, page=1, limit=100, name=None, modified_since=None, include_deprecated=False):
		"""Returns all customer data. Defaults to 1 page with 100 limit."""
		customer_url = self.url + "Customers"
		payload = {}
		payload["Page"] = page
		payload["Limit"] = limit
		if uuid:
			payload["ID"] = uuid
		if name:
			payload["Name"] = name
		if modified_since:
			try:
				d = datetime.strptime(modified_since, "%m-%d-%Y")
				since = d.isoformat()
				payload["ModifiedSince"] = since
			except:
				raise APIError("Error parsing the date. Please supply it in MM-DD-YYYY form.")
		if include_deprecated:
			payload["IncludeDeprecated"] = True
		self.r = requests.get(customer_url, headers=self.headers, params=payload)
		return self.r.json()



