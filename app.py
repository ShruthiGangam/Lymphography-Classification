from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('lympho.pkl','rb'))
@app.route('/')
def start():
   
    return render_template('index_main.html')
@app.route('/login', methods =['POST'])
def login():
 
    a = request.form["lymphatics"]
    
    b = request.form["block_of_affere"]
    
    c = request.form["bl._of_lymph._c"]
    
    d = request.form["bl._of_lymph._s"]
    
    e = request.form["by_pass"]
    
    f = request.form["extravasates"]
    
    g = request.form["regeneration"]
    
    h = request.form["early_uptake_in"]
    
    i = request.form["lym.nodes_dimin"]
    
    j = request.form["lym.nodes_enlar"]
    
    k = request.form["changes_in_lym"]
    
    l = request.form["defect_in_node"]
    
    m = request.form["changes_in_node"]
    
    n = request.form["changes_in_stru"]
    
    o = request.form["special_forms"]
    
    p = request.form["dislocation_of"]
    
    q = request.form["exclusion_of_no"]
    
    r = request.form["no_of_nodes_in"]
    
    
    if (a=="normal"):
        a=1
    elif(a=="arched"):
        a=2
    elif(a=="deformed"):
        a=3
    elif(a=="displaced"):
        a=4
    else:
        a=0

    if (b=="no"):
        b=1
    elif(b=="yes"):
        b=2
    else:
        b=0

    if (c=="no"):
        c=1
    elif(c=="yes"):
        c=2
    else:
        c=0

    if (d=="no"):
        d=1
    elif(d=="yes"):
        d=2
    else:
        d=0
    if (e=="no"):
        e=1
    elif(e=="yes"):
        e=2
    else:
        e=0

    if (f=="no"):
        f=1
    elif(f=="yes"):
        f=2
    else:
        f=0

    if (g=="no"):
        g=1
    elif(g=="yes"):
        g=2
    else:
        g=0

    if (h=="no"):
        h=1
    elif(h=="yes"):
        h=2
    else:
        h=0

    if (k=="bean"):
        k=1
    elif(k=="oval"):
        k=2
    elif(k=="round"):
        k=3
    else:
        k=0

    if (l=="no"):
        l=1
    elif(l=="lacunar"):
        l=2
    elif(l=="lac. marginal"):
        l=3
    elif(l=="lac. central"):
        l=4
    else:
        l=0

    if (m=="no"):
        m=1
    elif(m=="lacunar"):
        m=2
    elif(m=="lac. marginal"):
        m=3
    elif(m=="lac. central"):
        m=4
    else:
        m=0

    if (p=="no"):
        p=1
    elif(p=="yes"):
        p=2
    else:
        p=0

    if (q=="no"):
        q=1
    elif(q=="yes"):
        q=2
    else:
        q=0
    
    if (n=="no"):
        n=1  
    elif(n=="grainy"):
        n=2
    elif(n=="drop-like"):
        n=3
    elif(n=="coarse"):
        n=4
    elif(n=="diluted"):
        n=5
    elif(n=="reticular"):
        n=6
    elif (n=="stripped"):
        n=7
    elif (n=="faint"):
        n=8
    else:
        n=0
        
    if (o=="no"):
        o=1  
    elif(o=="chalices"):
        o=2
    elif(o=="vesicles"):
        o=3
    else:
        o=0

    if (r=="0-9"):
        r=1  
    elif(r=="10-19"):
        r=2
    elif(r=="20-29"):
        r=3
    elif(r=="30-39"):
        r=4
    elif(r=="40-49"):
        r=5
    elif(r=="50-59"):
        r=6
    elif (r=="60-69"):
        r=7
    elif (r==">=70"):
        r=8
    else:
        r=0
    
    t = [[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h),int(i),int(j),int(k),int(l),int(m),int(n),int(o),int(p),int(q),int(r)]] 
    
    output =model.predict(t)
    
    if (output[0]==1):
     return render_template("index_main.html", y = "The result shows that you are diagnosed as Normal")
    elif(output[0]==2):
        return render_template("index_main.html", y = "The result shows that you are diagnosed with Metastases")
    elif(output[0]==3):
       return render_template("index_main.html", y = "The result shows that you are diagnosed with  Malign Lymph")
    elif(output[0]==4):
       return render_template("index_main.html", y = "The result is shows that you are diagnosed with Fibrosis")

if __name__ == '__main__':  
    app.run(debug=True)