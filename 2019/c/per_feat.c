#include <stdio.h>
#include <string.h>

#define NUM_PFE       (2)
#define PFE_MASK      (8/ NUM_PFE)
#define PFE_FEAT_MASK (0xF)
enum {
    FIB_PER_FEAT_INC = 1,
    FIB_PER_FEAT_DEC = 2,
};

char per_ctx_feat[4096];

short
fib_is_per_ctx_feat(short pfe_id, short pd_fib_id)
{
    printf("%s: pfe:%d fib_id:%d feat:0x%02x-0x%02x\n", __func__,
            pfe_id, pd_fib_id,
            per_ctx_feat[pd_fib_id],
            (per_ctx_feat[pd_fib_id] & (PFE_FEAT_MASK << pfe_id)));

    return ((per_ctx_feat[pd_fib_id] & (PFE_FEAT_MASK << pfe_id)) == 0);
}

void
fib_oper_per_ctx_feat(short oper, short pfe_id, short pd_fib_id)
{
    char feat = per_ctx_feat[pd_fib_id];
    char pfe_feat;
    char mask_range = (PFE_MASK * pfe_id);

    printf("%s: oper:%d pfe:%d fib_id:%d feat:0x%02x-0x%02x\n", __func__,
            oper, pfe_id, pd_fib_id,
            per_ctx_feat[pd_fib_id],
            ((feat & (PFE_FEAT_MASK << pfe_id)) >> mask_range));

    pfe_feat = ((feat & (PFE_FEAT_MASK << mask_range)) >> mask_range);
    if (oper == FIB_PER_FEAT_INC) {
        pfe_feat++;
    } else {
        pfe_feat--;
    }

    feat &= ~(PFE_FEAT_MASK << mask_range);
    per_ctx_feat[pd_fib_id] = feat | (pfe_feat << mask_range);
    printf("%s: pfe_feat:%d feat:0x%02x\n",
            __func__, pfe_feat, per_ctx_feat[pd_fib_id]);
}

void
fib_inc_per_ctx_feat(short pfe_id, short pd_fib_id)
{
    fib_oper_per_ctx_feat(FIB_PER_FEAT_INC, pfe_id, pd_fib_id);
}

void
fib_dec_per_ctx_feat(short pfe_id, short pd_fib_id)
{
    fib_oper_per_ctx_feat(FIB_PER_FEAT_DEC, pfe_id, pd_fib_id);
}


void
test_set_feat(short pfe_id, short pd_fib_id)
{
    if (fib_is_per_ctx_feat(pfe_id, pd_fib_id)) {
        printf("create context\n");
    }

    fib_inc_per_ctx_feat(pfe_id, pd_fib_id);
    printf("%s done, pfe:%d fib_id:%d\n\n", __func__, pfe_id, pd_fib_id);
}

void
test_reset_feat(short pfe_id, short pd_fib_id)
{
    fib_dec_per_ctx_feat(pfe_id, pd_fib_id);

    if (fib_is_per_ctx_feat(pfe_id, pd_fib_id)) {
        printf("delete context\n");
    }
    printf("%s done, pfe:%d fib_id:%d\n\n", __func__, pfe_id, pd_fib_id);
}

int main()
{
    test_set_feat(0, 1);
    test_set_feat(1, 1);
    test_set_feat(0, 2);
    test_set_feat(1, 2);
    test_set_feat(0, 1);
    test_set_feat(1, 1);
    test_set_feat(0, 2);
    test_set_feat(1, 2);

    test_reset_feat(0, 1);
    test_reset_feat(1, 1);
    test_reset_feat(0, 2);
    test_reset_feat(1, 2);
    test_reset_feat(0, 1);
    test_reset_feat(1, 1);
    test_reset_feat(0, 2);
    test_reset_feat(1, 2);
}

