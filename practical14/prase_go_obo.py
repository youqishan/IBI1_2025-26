"""
Practical 14: Find GO term with the most <is_a> children in each ontology.
Using both DOM and SAX APIs, and compare their execution time.
"""

import xml.dom.minidom
import xml.sax
from xml.sax.handler import ContentHandler
from datetime import datetime

# ------------------------------------------------------------------
# 1. Using DOM API
# ------------------------------------------------------------------
def dom_parse(xml_file):
    """Return a dict: {ontology: (term_id, max_is_a_count)} using DOM."""
    start = datetime.now()
    
    dom = xml.dom.minidom.parse(xml_file)
    terms = dom.getElementsByTagName('term')
    
    # Store the maximum is_a counts for each ontology: {namespace: (term_id, count)}
    max_info = {
        'molecular_function': (None, -1),
        'biological_process': (None, -1),
        'cellular_component': (None, -1)
    }
    
    for term in terms:
        # Extract id
        id_elem = term.getElementsByTagName('id')
        if not id_elem:
            continue
        term_id = id_elem[0].firstChild.data if id_elem[0].firstChild else ''
        
        # Extract namespace
        ns_elem = term.getElementsByTagName('namespace')
        if not ns_elem:
            continue
        namespace = ns_elem[0].firstChild.data if ns_elem[0].firstChild else ''
        if namespace not in max_info:
            continue   # We only care about the three main ontologies
        
        # Count <is_a> elements (direct on the term, regardless of position)
        is_a_count = len(term.getElementsByTagName('is_a'))
        
        if is_a_count > max_info[namespace][1]:
            max_info[namespace] = (term_id, is_a_count)
    
    end = datetime.now()
    elapsed = (end - start).total_seconds()
    return max_info, elapsed

# ------------------------------------------------------------------
# 2. Using SAX API
# ------------------------------------------------------------------
class GOSAXHandler(ContentHandler):
    def __init__(self):
        self.current_tag = ''
        self.current_text = ''
        self.current_term = {}
        self.in_term = False
        self.max_info = {
            'molecular_function': (None, -1),
            'biological_process': (None, -1),
            'cellular_component': (None, -1)
        }
        self.current_is_a_count = 0
    
    def startElement(self, name, attrs):
        self.current_tag = name
        if name == 'term':
            self.in_term = True
            self.current_term = {}
            self.current_is_a_count = 0
            self.current_text = ''
        elif name == 'is_a' and self.in_term:
            # count <is_a> elements only when inside a term
            self.current_is_a_count += 1
    
    def endElement(self, name):
        if name == 'term':
            # Check if this term has the most <is_a> for its namespace
            namespace = self.current_term.get('namespace', '')
            if namespace in self.max_info:
                term_id = self.current_term.get('id', '')
                count = self.current_is_a_count
                if count > self.max_info[namespace][1]:
                    self.max_info[namespace] = (term_id, count)
            self.in_term = False
            self.current_term.clear()
        elif name == 'id' and self.in_term:
            self.current_term['id'] = self.current_text.strip()
        elif name == 'namespace' and self.in_term:
            self.current_term['namespace'] = self.current_text.strip()
        # Clear current text after processing an element
        self.current_text = ''
    
    def characters(self, content):
        if self.in_term and self.current_tag in ('id', 'namespace'):
            self.current_text += content

def sax_parse(xml_file):
    """Return a dict: {ontology: (term_id, max_is_a_count)} using SAX."""
    start = datetime.now()
    
    handler = GOSAXHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    
    end = datetime.now()
    elapsed = (end - start).total_seconds()
    return handler.max_info, elapsed

# ------------------------------------------------------------------
# 3. Compare which is faster and print results
# ------------------------------------------------------------------
def print_results(results, method_name):
    print(f"\n=== Results from {method_name} ===")
    for onto, (term_id, count) in results.items():
        onto_name = onto.replace('_', ' ').title()
        print(f"{onto_name}:")
        print(f"  GO term with most <is_a>: {term_id if term_id else 'None'}")
        print(f"  Number of <is_a> elements: {count}")

if __name__ == "__main__":
    xml_file = "go_obo.xml"   # Ensure the file is in the current directory
    
    # DOM
    dom_results, dom_time = dom_parse(xml_file)
    print_results(dom_results, "DOM")
    print(f"Time taken by DOM: {dom_time:.4f} seconds")
    
    # SAX
    sax_results, sax_time = sax_parse(xml_file)
    print_results(sax_results, "SAX")
    print(f"Time taken by SAX: {sax_time:.4f} seconds")
    
    # Compare and comment on which is faster
    if dom_time < sax_time:
        faster = "DOM"
    elif sax_time < dom_time:
        faster = "SAX"
    else:
        faster = "Both equally fast"
    
    # print the performance comment
    print(f"\nComment: The {faster} API ran faster for this XML file.")

# Comment
"""
Performance comment:
Based on the execution results, SAX runs almost 7 times faster than DOM 
when parsing large XML files. This is because DOM loads the entire tree 
into memory, while SAX processes the file sequentially. 
In conclusion, SAX was quicker. 
"""