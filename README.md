AutoTaxonomyExtractionAndTagging
================================


To start Solr:

    cd solr_example_dir
    java -jar -Dsolr.solr.home=<full_path_to_this_dir>/solr_home start.jar


To index documents:

    python extractDocs.py "<full_path_to_stack_exchange_dump>/posts.xml" | curl -d @- http://localhost:8983/solr/update?commit=true -v -H "Content-Type:text/xml"

testtoken1
testtoken2
testtoken3
testtoken4
testtoken5

