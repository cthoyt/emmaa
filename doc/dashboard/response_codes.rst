.. _fail_result:

Failing test/query result interpretation
========================================
Model tests and queries can sometimes fail to produce an explicit result (i.e.,
a sequence of mechanisms constituting an answer to a query). There are several
possible reasons for this. Below, we explain the various result "codes" that
can appear on the model tests and query pages.

  - **Path found but exceeds search depth** - Path is found, but the search
    depth is reached. Search depth is the maximum number of steps taken to
    reach the object from the subject in the graph representation of the model.
  - **Statement subject not in model** - The subject of the query or
    statement doesn't exist in the model.
  - **Statement object state not in model** - The object state of the
    query or statement does not exist in the model.
  - **Query is not applicable for this model** - Only used for queries.
  - **No path found that satisfies the test statement** - Only used for tests.
  - **Statement type not handled** - The statement type is not valid.
    Currently supported types:

    + Activation
    + Inhibition
    + IncreaseAmount
    + DecreaseAmount
    + Acetylation
    + Farnesylation
    + Geranylgeranylation
    + Glycosylation
    + Hydroxylation
    + Methylation
    + Myristoylation
    + Palmitoylation
    + Phosphorylation
    + Ribosylation
    + Sumoylation
    + Ubiquitination
    + Deacetylation
    + Defarnesylation
    + Degeranylgeranylation
    + Deglycosylation
    + Dehydroxylation
    + Demethylation
    + Demyristoylation
    + Depalmitoylation
    + Dephosphorylation
    + Deribosylation
    + Desumoylation
    + Deubiquitination
