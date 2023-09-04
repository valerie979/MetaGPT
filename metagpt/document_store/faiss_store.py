# ... existing code ...

class FaissStore(LocalStore):
    # ... existing code ...

    def search(self, query, expand_cols=False, sep='\n', *args, k=5, **kwargs):
        rsp = self.store.similarity_search(query, k=k, **kwargs)
        logger.debug(rsp)
        if expand_cols:
            return str(sep.join([f"{x.page_content}: {x.metadata}" for x in rsp]))
        else:
            return str(sep.join([f"{x.page_content}" for x in rsp]))

    # ... existing code ...