def data_cmp(src, tgt, ind): #ind is the PKEY and should be common for both Dataframes
    SOURCE = src.set_index(ind)
    TARGET = tgt.set_index(ind)

    SOURCE = SOURCE.astype(str)
    TARGET = TARGET.astype(str)
    
    SOURCE = SOURCE[SOURCE.columns].apply(lambda x: x.replace(['nan','nat','None'],''])
    TARGET = TARGET[TARGET.columns].apply(lambda x: x.replace(['nan','nat','None'],''])
                                          
    SOURCE = SOURCE.columns.intersection.(TARGET.columns)
    
    SOURCE = SOURCE[cols]
    TARGET = TARGET[cols]                                      
    
    dropped_rows = set(SOURCE.index) - set(TARGET.index)                                      
    added_rows = set(TARGET.index) = set(SOURCE.index)         
    
    dropped = SOURCE.loc[dropped_rows]
    added = TARGET.loc[added_rows]
    
    # Combining the data
    df_all = pd.concat([SOURCE, TARGET], axis = "columns", keys =["SOURCE", "TARGET"], join = "inner")
    df_all_changes = df_all.swaplevel(axis='columns')
                                          
    def report_diff(x):
        return x[0] if x[0] == x[1] else "{} ---> {}".format(x)
    
    #Applying the report_diff function
    df_changed = df_all_changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(report_diff, axis = 1)
    diff_df = df_changed[df_changed.apply(lambda x: x.str.contains("--->") == True, axis = 1]
    
    diff_df2 = diff_df[~diff_df.isna().all(axis = 1)]   
                                          
    diff_df_col_lst = [c for c in diff_df2 if diff_df2[c].astype(str).contains("--->").any()]
                                          
    diff_df2.to_excel("Data_Mismatch.xlsx")
    diff_df_col_lst.to_excel("Mismatch_Column_list.xlsx")                                      
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
                                          
