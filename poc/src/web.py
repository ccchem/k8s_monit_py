import k8s.client
from flask import Flask, render_template, request

#----------------------------------------------------------

# Init Kubernetes API reader
rd = k8s.client.Client()

# Create Flask app
app = Flask("cms-monit")

# HTTP request handlers
@app.route('/')
def index():
  # Parse URL parameters
  showContainers = False
  param = request.args.get('view')
  if param and param == "containers":
    showContainers = True

  # Get pods
  status, data = rd.get_pods()

  # Show results  
  if status:
    return render_template("index.html", pods=data, withContainers=showContainers)
  else:
    print(data)
    return "Error calling Kubernetes API."

#----------------------------------------------------------

# Dev only. Run Flask app
if __name__ == "__main__":
  app.run(host= "0.0.0.0")

